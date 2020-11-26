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

class ActionGetInformacoes(Action):

    def name(self) -> Text:
        return "action_get_informacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tipo = None
        numero = None
        data = None

        for entity in tracker.latest_message['entities']:
            if entity['entity'] == 'tipo':
                tipo = entity['value']
            elif entity['entity'] == 'numero':
                numero = entity['value']
            elif entity['entity'] == 'dia_mes':
                data = entity['value'][3:] + '/' + entity['value'][:2]

        if data:
            valor = data
        else:
            valor = numero

        text = buscaInformacoes(tipo, valor)
        # text = traduzTexto(text, api_key)
        
        retorno_debug = f'Tipo: {tipo}; Número: {numero}; Data: {data}'
        dispatcher.utter_message(text=retorno_debug)

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
# def traduzTexto(text, api_key):
#     translator = LanguageTranslatorV3(
#             version='2020-11-04',
#             iam_apikey=api_key
#         )
        
#     response = translator.translate(
#             text,
#             source='en',
#             target='pt-br'
#         )
#     res = response.get_result()
#     retorno = res['translations'][0]['translation']
    
#     return retorno