## Generated Story -4876079331474673216
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_restaurant
    - utter_ask_about_emailing
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_validate_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - utter_goodbye
    - export

## Generated Story 1534185993162834312
* goodbye
    - utter_greet
* goodbye
    - export

## Generated Story 6873553703660392431
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_validate_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "mid"}
    - utter_ask_about_emailing
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_validate_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - utter_goodbye
    - export

## Generated Story -1896865454489331680
* greet
    - utter_greet
* restaurant_search
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - action_validate_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "low"}
    - utter_ask_about_emailing
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_validate_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - utter_goodbye
    - export

## Generated Story -752691597551468943
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - action_check_budget
    - slot{"budget": "low"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "low"}
    - utter_ask_mailing
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - slot{"email": "rahanapa@gmail.com"}
    - utter_goodbye
    - export

## Generated Story 4852430569982092946
* 
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300 - 700"}
    - slot{"budget": "300 - 700"}
    - action_check_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "mid"}
    - utter_ask_mailing
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - utter_ask_mailid
* send_email{"email": "rahanapa@gmailcom"}
    - slot{"email": "rahanapa@gmailcom"}
    - action_check_email
    - slot{"email": null}
    - action_email
    - utter_goodbye
    - export

## Generated Story -1432886952426132575
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_check_budget
    - slot{"budget": "mid"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "mid"}
    - utter_ask_mailing
* send_email
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - utter_ask_mailid
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_check_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - slot{"email": "rahanapa@gmail.com"}
    - utter_goodbye
    - export

