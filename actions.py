# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List, Union

from rasa_core_sdk.events import UserUtteranceReverted, SlotSet
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd


filen = "C:\\pyth\\pyhton\\rabot\\chart symptoms1.xlsx"
df = pd.read_excel(filen)


# print(df)


# symptom='redness of eye(s)'
# symptom1='irritation of eyes'
# symptom2='light sensitivity'

def passing(symp,symp1,symp2):
    def final_index(out):
        return max(set(out), key=out.count)
    out = []

    # to check presence
    result = df.isin([symp])
    result1 = df.isin([symp1])
    result2 = df.isin([symp2])
    # to find coloumns
    disobj = result.any()
    disobj1 = result1.any()
    disobj2 = result2.any()
    columnnames = list(disobj[disobj == True].index)
    for col in columnnames:
        rows = list(result[col][result[col] == True].index)
        #   print(rows)
        for row in rows:
            out.append(row)
            print("H", row)
    columnnames = list(disobj1[disobj1 == True].index)
    for col in columnnames:
        rows = list(result1[col][result1[col] == True].index)
        #       print(rows1)
        for row in rows:
            out.append(row)
            print("M", row)
    columnnames = list(disobj2[disobj2 == True].index)
    for col in columnnames:
        rows = list(result2[col][result2[col] == True].index)
        #       print(rows1)
        for row in rows:
            out.append(row)
            print("L", row)
    print(final_index(out))
    global disease
    disease = (df.iloc[final_index(out)]['Diseases'])

    print(disease)


class ActionisBOT(Action):
    def name(self):
        return "action_is_bot"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_is_bot", tracker)
        return [UserUtteranceReverted()]


class Medical(Action):
    def name(self) -> Text:
        return "action_disease"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        symptom = tracker.get_slot("symptom")
        symptom1 = tracker.get_slot("symptom1")
        symptom2 = tracker.get_slot("symptom2")
        name = tracker.get_slot("name")
        passing(symptom,symptom1,symptom2)
        if disease:
            dispatcher.utter_message("hey,by your symptoms of {},{},{} you may have {}".format(symptom, symptom1, symptom2, disease))
        else:
            dispatcher.utter_template("utter_default", tracker)

        return [SlotSet("disease", disease)]
