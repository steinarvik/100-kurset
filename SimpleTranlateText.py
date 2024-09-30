import requests

text_to_translate = "How are you?"
target_language = 'IT'

url = "https://api-free.deepl.com/v2/translate"
api_key = "5b214a2b-4906-42ea-bdb3-862026badf48:fx"

params = {
    'auth_key': api_key,
    'text': text_to_translate,
    'target_lang': target_language
}

response = requests.get(url, data=params)
result = response.json()