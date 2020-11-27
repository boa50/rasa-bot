# Instalação das dependências

**Spacy**
- $pip3 install rasa[spacy]
- $python3 -m spacy download en_core_web_md
- $python3 -m spacy link en_core_web_md en

**LanguageTranslatorV3**
- $pip install ibm-watson
- É preciso ter um cadastro no serviço IBM Language Translator: https://www.ibm.com/watson/services/language-translator/
- Renomear o arquivo actions/config.ini_example para actions/config.ini, copiar a api-key para a o campo *api-key* dentro desse novo arquivo.

# Comandos a serem executados
- $rasa train (para realizar o treinamento inicial do modelo)
- $rasa run actions (para disponibilizar as ações customizadas através do endereço http://localhost:5055/webhook)
- $rasa shell (para fazer os testes iniciais com o bot)