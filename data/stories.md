##story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
	- slot{"location": "bangalore"}
	- action_check_location
	- slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
	- slot{"cuisine": "Chinese"}
    - action_check_cuisine
	- slot{"cuisine": "Chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
	- action_check_budget
	- slot{"budget": "low"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two people less than 300"}
	- utter_ask_mailing
* affirm
    - utter_ask_mailid
* send_email{"email": "axyz@gmail.com"}
	- slot{"email": "axyz@gmail.com"}
	- action_check_email
	- slot{"email": "axyz@gmail.com"}
	- action_email
	- slot{"email": "axyz@gmail.com"}
	- utter_goodbye
    - action_restarted
	
## story 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
	- slot{"location": "pune"}
	- action_check_location
	- slot{"location": "pune"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
	- slot{"cuisine": "South Indian"}
    - action_check_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "> 700"}
    - slot{"budget": "> 700"}
	- action_check_budget
	- slot{"budget": "high"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two > 700"}
	- utter_ask_mailing
* affirm
    - utter_ask_mailid
* send_email{"email": "axyz@gmail.com"}
	- slot{"email": "axyz@gmail.com"}
 	- action_check_email
	- slot{"email": "axyz@gmail.com"}
	- action_email
	- slot{"email": "axyz@gmail.com"}
	- utter_goodbye
    - action_restarted	
	
## story 3
* greet
    - utter_greet
* deny
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Gangtok"}
	- slot{"location": "Gangtok"}
    - action_check_location
	- slot{"location": null}
    - utter_ask_location    
* restaurant_search{"location": "chennai"}
	- slot{"location": "chennai"}
    - action_check_location
	- slot{"location": "chennai"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
	- slot{"cuisine": "Chinese"}
    - action_check_cuisine
	- slot{"cuisine": "Chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "300 - 700"}
    - slot{"budget": "300 - 700"}
	- action_check_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two people between 300 to 700"}
	- utter_ask_mailing
* affirm
    - utter_ask_mailid
* send_email{"email": "xyz.gmail.com"}
	- slot{"email": "xyz.gmail.com"}
	- action_check_email
	- slot{"email": null}
	- utter_ask_mailid
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
	- action_check_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
	
## story 4

* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Spanish"}
	- slot{"cuisine": "Spanish"}
	- action_check_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- action_check_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "> 700"}
    - slot{"budget": "> 700"}
	- action_check_budget
	- slot{"budget": "mid"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two > 700"}
	- utter_ask_mailing
* affirm
    - utter_ask_mailid
* send_email{"email": "xyz@test.com"}
	- slot{"email": "xyz@test.com"}
    - action_check_email
	- slot{"email": "xyz@test.com"}
	- action_email
	- slot{"email": "xyz@test.com"}
	- utter_goodbye
    - action_restarted
	

## story 5

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
	- slot{"location": "agra"}
	- action_check_location
	- slot{"location": "agra"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
	- slot{"cuisine": "Italian"}
    - action_check_cuisine
	- slot{"cuisine": "Italian"}
	- utter_ask_budget
* restaurant_search{"budget": "< 300"}
    - slot{"budget": "< 300"}
	- action_check_budget
	- slot{"budget": "low"}
	- utter_top_restaurant
	- action_restaurant
    - slot{"budget": "average cost for two people less than 300"}
	- utter_ask_mailing
* deny
    - utter_goodbye
	- export
	

## Story 6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": null}
	- slot{"location": null}
	- action_check_location
	- slot{"location": null}
	- utter_ask_location
* restaurant_search{"location": null}
	- slot{"location": null}
	- action_check_location
	- slot{"location": null}
	- utter_goodbye
	
## story 7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
	- slot{"location": "hyderabad"}
	- action_check_location
	- slot{"location": "hyderabad"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "spanish"}
	- slot{"cuisine": "spanish"}
	- action_check_cuisine
	- slot{"cuisine": null}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "spanish"}
	- slot{"cuisine": "spanish"}
	- action_check_cuisine
	- slot{"cuisine": null}
    - utter_goodbye
	- action_restarted
	
