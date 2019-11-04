## Generated Story -5338494287190991486
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
    - slot{"budget": "low"}
    - utter_ask_about_emailing
* send_email{"email": "rahanapa@gmail.com"}
    - slot{"email": "rahanapa@gmail.com"}
    - action_validate_email
    - slot{"email": "rahanapa@gmail.com"}
    - action_email
    - utter_goodbye
    - export

