import requests

text_to_translate = input("Enter text:")
target_language = input("enter target language (code)")

url = "https://api-free.deepl.com/v2/translate"
api_key = "5b214a2b-4906-42ea-bdb3-862026badf48:fx"

params = {
    'auth_key': api_key,
    'text': text_to_translate,
    'target_lang': target_language
}

response = requests.get(url, data=params)
result = response.json()
translated_text = result['translations'][0]['text']

print(f"Translated text: {translated_text} ")