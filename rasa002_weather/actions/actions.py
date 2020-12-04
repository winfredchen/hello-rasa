# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .weather import Weather


class ActionWeatherAPI(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.latest_message['text'] # 获取上一步输入的城市（未做优化判断是否是城市等）
        temp = int(Weather(city)['temp'] - 273) # 调用接口获取
        dispatcher.utter_template("utter_temp",tracker,temp = temp) # 传递到response中

        return []
