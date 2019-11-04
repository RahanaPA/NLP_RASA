## Generated Story 2930213521206069221
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - action_validate_budget
    - slot{"budget": "high"}
    - utter_top_restaurant
    - action_restaurant
    - slot{"budget": "high"}
    - utter_ask_about_emailing
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_validate_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - slot{"email": "rahanapa@gmail.com"}
    - export

## Generated Story 646968006146698975
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
    - action_check_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - slot{"email": "rahanapa@gmail.com"}
    - utter_goodbye
    - export

## Generated Story -4135302660667378483
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
* out_of_scope
    - utter_ask_mailid
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_check_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - slot{"email": "rahanapa@gmail.com"}
    - export

