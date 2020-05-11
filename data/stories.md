
## bot challenge
* bot_challenge
   - utter_iamabot
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
* request disease{"symptom1": "cold"}
   - slot{"symptom1": "cold"}
   - utter_ask_symptoms
* request disease{"symptom1": "light body pains"}
   - slot{"symptom1": "light body pains"}
   - action_disease
* accept
   - utter_goodbye

## interactive_story_1
* greetings
   - utter_greet
   - utter_ask_name
* greetings{"name": "harish"}
   - slot{"name": "harish"}
   - utter_howcanhelp
* request disease{"symptom": "headache"}
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

## interactive_story_1
* greetings
    - utter_greet
    - utter_ask_name
* give Information{"name": "rajesh"}
    - slot{"name": "rajesh"}
    - utter_howcanhelp
* request disease{"symptom1": "vomitings", "symptom": "headache"}
    - slot{"symptom": "headache"}
    - slot{"symptom1": "vomitings"}
    - utter_ask_symptoms
* request disease{"symptom2": "jaundice"}
    - slot{"symptom2": "jaundice"}
    - action_disease
    - slot{"disease": "Hepatitis"}
* thanks
    - utter_thanks

## interactive_story_1
* greetings
    - utter_greet
    - utter_ask_name
* give Information{"name": "suresh"}
    - slot{"name": "suresh"}
    - utter_howcanhelp
* request disease{"symptom1": "cold"}
    - slot{"symptom1": "cold"}
    - utter_ask_symptoms
* request disease{"symptom": "body pains"}
    - slot{"symptom": "body pains"}
    - action_disease
* thanks
    - utter_thanks

## interactive_story_1
* greetings
    - utter_greet
    - utter_ask_name
* give Information{"name": "gayathri"}
    - slot{"name": "gayathri"}
    - utter_howcanhelp
* request disease{"symptom1": "vomitings"}
    - slot{"symptom1": "vomitings"}
    - utter_ask_symptoms
* request disease{"symptom2": "jaundice"}
    - slot{"symptom2": "jaundice"}
    - action_disease
    - slot{"disease": "Hepatitis"}

## interactive_story_1
* bot_challenge
    - utter_iamabot
    - utter_howcanhelp
* request disease{"symptom": "nasal discharge", "symptom1": "dry cough"}
    - slot{"symptom": "nasal discharge"}
    - slot{"symptom1": "dry cough"}
    - utter_ask_symptoms
* request disease{"symptom2": "sore throat"}
    - slot{"symptom2": "sore throat"}
    - action_disease
    - slot{"disease": "Influenza (flu)"}
* accept
    - utter_goodbye
