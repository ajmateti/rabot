# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []

class ActionFormInfo(FormAction):
    def name(self) -> Text:
        return "symptoms_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "symptom", "symptom1", "symptom2"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit", name=tracker.get_slot('name'),
                                 symptom=tracker.get_slot('symptom'), symptom1=tracker.get_slot('symptom1'),
                                 symptom2=tracker.get_slot('symptom2'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": self.from_entity(entity="name", intent='greetings'),
            "symptom": self.from_entity(entity='symptom', intent='request disease'),
            "symptom1": self.from_entity(entity='symptom1', intent='request disease'),
            "symptom2": self.from_entity(entity='symptom2', intent='request disease'),

        }
