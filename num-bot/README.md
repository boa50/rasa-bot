# Instalação das dependências

**Spacy**
- $pip3 install rasa[spacy]
- $python3 -m spacy download en_core_web_md
- $python3 -m spacy link en_core_web_md en

**LanguageTranslatorV3**
- $pip install ibm-watson
- *É preciso ter um cadastro no serviço IBM Language Translator: https://www.ibm.com/watson/services/language-translator/*
- Copiar a api-key para a variável *api_key* dentro da função *traduzTexto* no arquvio actions/actions.py