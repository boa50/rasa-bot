# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
from configparser import ConfigParser

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class ActionGetInformacoes(Action):

    def name(self) -> Text:
        return "action_get_informacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tipo = next(tracker.get_latest_entity_values('tipo'), None)
        numero = next(tracker.get_latest_entity_values('numero'), None)
        data = next(tracker.get_latest_entity_values('dia_mes'), None)

        if data:
            valor = data[3:] + '/' + data[:2]
        else:
            valor = numero

        text = buscaInformacoes(tipo, valor)
        text = traduzTexto(text)

        dispatcher.utter_message(text=text)
        
        # retorno_debug = f'Tipo: {tipo}; Número: {numero}; Data: {data}'
        # dispatcher.utter_message(text=retorno_debug)

        return []

class ActionGetOutrasInformacoes(Action):

    def name(self) -> Text:
        return "action_get_outras_informacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = buscaInformacoes()
        text = traduzTexto(text)

        dispatcher.utter_message(text=text)

        return []

### Realiza as conexões com a numbers api
def buscaInformacoes(tipo='trivia', valor=None):
    if valor == None:
        valor = 'random'
        
    url = f'http://numbersapi.com/{valor}/{tipo}'
    
    response = requests.request("GET", url)
    
    return response.text

### Utilizado para traduzir os textos de retorno da api
def traduzTexto(text):
    config_object = ConfigParser()
    config_object.read('actions/config.ini')
    api_key = config_object['TRANSLATOR']['api-key']

    authenticator = IAMAuthenticator(api_key)
    translator = LanguageTranslatorV3(
            version='2020-11-04',
            authenticator=authenticator
        )
        
    response = translator.translate(
            text,
            source='en',
            target='pt-br'
        )
    res = response.get_result()
    retorno = res['translations'][0]['translation']
    
    return retorno