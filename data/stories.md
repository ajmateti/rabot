
## say goodbye
* goodbye
   - utter_goodbye

## bot challenge
* bot_challenge
   - utter_iamabot
* greetings
   - utter_howcanhelp
* request information
   - action_disease
   - utter_submit
* goodbye
   - utter_goodbye
## story_003
* greetings
   - utter_greet
   - utter_ask_name
* request information
   - utter_ask_symptoms
   - action_disease
   - utter_goodbye
## story_004
* greetings
   - utter_greet
## interactive_story_2
* greetings{"name": "harish"}
   - slot{"name": "harish"}
   - utter_howcanhelp
* request disease{"symptom": "stomach pain"}
   - slot{"symptom": "stomach pain"}
   - action_disease
## story_005
* greetings
   - utter_greet
   - utter_ask_name
## story_007
* greetings{"name": "harish"}
   - slot{"name": "harish"}
   - utter_howcanhelp
* request disease{"symptom": "stomach pain"}
   - slot{"symptom": "stomach pain"}
   - action_disease
* goodbye
   - utter_goodbye
## story_006
 * thanks
   - utter_thanks 
## interactive_story_1
* greetings
   - utter_greet
   - utter_ask_name
* request disease,prescription{"symptom1": "cold"}
   - slot{"symptom1": "cold"}
   - action_disease
* accept
   - utter_goodbye

## interactive_story_1
* request disease,prescription{"symptom": "fever"}
   - slot{"symptom": "fever"}
   - action_disease
* thanks
   - utter_thanks

## interactive_story_1
* request disease{"symptom": "headache"}
   - slot{"symptom": "headache"}
   - action_disease

## interactive_story_2
* request disease{"symptom": "headache"}
   - slot{"symptom": "headache"}
   - action_disease
## interactive_story_3
* greetings
   - utter_greet
   - utter_ask_name
* greetings{"name": "harish"}
   - slot{"name": "harish"}
   - utter_howcanhelp
* request disease,prescription{"symptom": "headache"}
   - slot{"symptom": "headache"}
   - action_disease
* goodbye
   - utter_goodbye

 
## interactive_story_1
* greetings
    - utter_greet
    - utter_ask_name
* give Information{"name": "hari"}
    - slot{"name": "hari"}
    - utter_howcanhelp
* request disease{"symptom": "irritation of eyes"}
    - slot{"symptom": "irritation of eyes"}
    - utter_ask_symptoms
* request disease{"symptom2": "redness of eyes"}
    - slot{"symptom2": "redness of eyes"}
    - utter_ask_symptoms
* request disease{"symptom1": "light sensitivity"}
    - slot{"symptom1": "light sensitivity"}
    - action_disease
* thanks
    - utter_thanks

## interactive_story_1
* greetings{"name": "chandu"}
    - slot{"name": "chandu"}
    - utter_howcanhelp
* request disease{"symptom": "irritation of eyes", "symptom2": "redness of eyes", "symptom1": "light sensitivity"}
    - slot{"symptom": "irritation of eyes"}
    - slot{"symptom1": "light sensitivity"}
    - slot{"symptom2": "redness of eyes"}
    - action_disease
    - slot{"disease": "Conjunctivitis (pink eye)"}
* thanks
    - utter_thanks
