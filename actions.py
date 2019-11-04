from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import Restarted
from collections import OrderedDict
import zomatopy
import json
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f1955113769a9fec72633a83dcf09c91"}#type your zomato API key here
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		cuisine = cuisine.lower()
		
		budget = tracker.get_slot('budget')
		if budget == 'low':
			min_range = 0
			max_range = 300
		elif budget == 'mid':
			min_range = 301
			max_range = 700
		elif budget == 'high':
			min_range = 701
			max_range = 9999
		
		rest_df = pd.DataFrame(columns = ['Restaurant Name', 'Restaurant Location', 'Average Budget for two people', 'Zomato Rating'])
		location_detail=zomato.get_location(loc, 1)
		
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,
						'mexican':73,
						'italian':55,
						'american':1,
						'north indian':50,
						'south indian':85}
		
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)
		response=""
		for i in range(0,5, 1):
			d = json.loads(results[i])
			
			if d["results_found"] == 0:
				response= "Sorry, we didn't find any results for this query."
			else:
			
				for restaurant in d['restaurants']:
					res = {'Restaurant Name':restaurant['restaurant']['name'],
							'Restaurant Location': restaurant['restaurant']['location']['address'],
							'Average Budget for two people':restaurant['restaurant']['average_cost_for_two'],
							'Zomato Rating':restaurant['restaurant']['user_rating']['aggregate_rating']}
							
					avg_c_2 = res['Average Budget for two people']		
					if (avg_c_2 >= min_range) and (avg_c_2 <= max_range):						
						rest_df.loc[len(rest_df)] = res
			 
		rest_df = rest_df.sort_values(['Zomato Rating','Average Budget for two people'], ascending=[False,True])
		
		rest_df = rest_df.reset_index(drop=True)
		rest_df.index = rest_df.index.map(str)

		if len(rest_df) == 0:
			response = 'Sorry could not find any restaurants in this budget range'
		else:
			for index, row in rest_df.head(5).iterrows():
				response = response+ index + ". Found \""+ row['Restaurant Name']+ "\" in "+ row['Restaurant Location']+" has been rated "+ row['Zomato Rating']+"\n"
			
		dispatcher.utter_message(response)
		return [SlotSet('budget',budget)]
		
class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		cities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
						"Agra","Ajmer","Aligarh","Allahabad","Amravati","Amritsar","Asansol","Aurangabad",
						"Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar",
						"Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
						"Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
						"Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati",
						"Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur",
						"Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
						"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
						"Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry","Raipur","Rajkot",
						"Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri",
						"Solapur","Srinagar","Sultanpur","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur",
						"Ujjain","Vijayapura","Vadodara","Varanasi",
						"Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]
						
		cities_list = [x.lower() for x in cities]
		loc = tracker.get_slot('location')
		if(loc == None):
			dispatcher.utter_template("utter_location_not_found",tracker)
			return [SlotSet('location',None)]
		elif(loc.lower() not in cities_list):
			dispatcher.utter_template("utter_location_not_found",tracker)
			return [SlotSet('location',None)]
		else:
			return [SlotSet('location',loc)]

class ActionCheckCuisine(Action):
	def name(self):
		return 'action_check_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		cuisine_lst = ["chinese","mexican","american","italian","south indian","north indian"]
		cuisine = tracker.get_slot('cuisine')
		if(cuisine == None):
			dispatcher.utter_template("utter_cusine_not_found",tracker)
			return [SlotSet('cuisine',None)]
		elif(cuisine.lower() not in cuisine_lst):
			dispatcher.utter_template("utter_cusine_not_found",tracker)
			return [SlotSet('cuisine',None)]
		else:
			return [SlotSet('cuisine',cuisine)]			
	
class ActionCheckBudget(Action):
	def name(self):
		return 'action_check_budget'
		
	def run(self, dispatcher, tracker, domain):
		budget_range = tracker.get_slot('budget')
		if budget_range == 'less than 300' or budget_range == 'lesser than 300' or budget_range == '< 300'or ("cheap" in budget_range):
			return[SlotSet('budget', 'low')]
		elif budget_range == 'more than 700'or budget_range == 'greater than 700' or budget_range == '> 700' or ("costly" in budget_range) or ("expensive" in budget_range):
			return[SlotSet('budget', 'high')]
		else:
			return[SlotSet('budget', 'mid')]
	
class ActionCheckEmailId(Action):
	def name(self):
		return 'action_check_email'
		
	def run(self, dispatcher, tracker, domain):
		pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
				
		email = tracker.get_slot('email')
		if email is not None:
			if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
				return[SlotSet('email',email)]
			else:
				dispatcher.utter_message("Email not recognised. please type again")
				return[SlotSet('email',None)]
		else:
			dispatcher.utter_message("Please provide Email id again")
			return[SlotSet('email', None)]			
	

class ActionSendEmail(Action):
	def name(self):
		return 'action_email'		
    		
	def run(self, dispatcher, tracker, domain):
		config={"user_key":"f1955113769a9fec72633a83dcf09c91"}#type your zomato API key here
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		cuisine = cuisine.lower()
		budget = tracker.get_slot('budget')
		
		if budget == 'low':
			min_range = 0
			max_range = 300
		elif budget == 'mid':
			min_range = 301
			max_range = 700
		elif budget == 'high':
			min_range = 701
			max_range = 9999
		
		rest_dfMail = pd.DataFrame(columns = ['Restaurant Name', 'Restaurant Location', 'Average Budget for two people', 'Zomato Rating'])
		location_detail=zomato.get_location(loc, 1)
		
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,
						'mexican':73,
						'italian':55,
						'american':1,
						'north indian':50,
						'south indian':85}
		
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)
		response=""
		for i in range(0,5, 1):
			d = json.loads(results[i])
			
			if d["results_found"] == 0:
				response= "Sorry, we didn't find any results for this query."
			else:
			
				for restaurant in d['restaurants']:
					resMail = {'Restaurant Name':restaurant['restaurant']['name'],
								'Restaurant Location': restaurant['restaurant']['location']['address'],
								'Average Budget for two people':restaurant['restaurant']['average_cost_for_two'],
								'Zomato Rating':restaurant['restaurant']['user_rating']['aggregate_rating']}
					avg_c_2 = resMail['Average Budget for two people']		
					if (avg_c_2 >= min_range) and (avg_c_2 <= max_range):						
						rest_dfMail.loc[len(rest_dfMail)] = resMail			
					
		rest_dfMail = rest_dfMail.sort_values(['Zomato Rating','Average Budget for two people'], ascending=[False,True])
		
		email = tracker.get_slot('email')
		user_id = 'upgradcasestudy@gmail.com'  #type your email id here
		user_pwd = 'cohortiiit2018' #type your password here
		
		message = MIMEMultipart('alternative')
		message['Subject'] = "Restaurant Details"
		message['From'] = user_id
		message['To'] = str(email)
		
		if len(rest_dfMail) != 0:
			rest_dfMail10 = rest_dfMail.head(10)
			rest_dfMail10 = rest_dfMail10.reset_index(drop=True)
			rest_dfMail10.index = rest_dfMail10.index.map(str)
			html = """
			<html>
			<body>
			<p>The details of all the restaurants you inquried.</p>
			"""
			html = html+rest_dfMail10.to_html()
		else:
			
			html = """
			<html>
			<body>
			<p>Sorry... We could not find the details of restaurants you enquired.</p>	
			"""	
			
		html_body = html
		
		txtmsg = MIMEText(html_body, 'html')
		message.attach(txtmsg)
		server = smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.ehlo()
		server.login(user_id, user_pwd)
		server.sendmail(user_id, str(email), message.as_string())
		server.close()
		dispatcher.utter_message("Email Sent to "+email)
		
		
		return [SlotSet('email',email)]
		
class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()] 
