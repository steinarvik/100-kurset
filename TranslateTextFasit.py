import requests

# Get user inputs
text_to_translate = input("Enter text: ")
target_language = input("Enter target language (e.g., IT for Italian): ")

# DeepL API URL and API key
url = "https://api-free.deepl.com/v2/translate"
api_key = '5b214a2b-4906-42ea-bdb3-862026badf48:fx'

# Parameters for the API request
params = {
    'auth_key': api_key,
    'text': text_to_translate,
    'target_lang': target_language
}

# Send the request and get the response
response = requests.get(url, data=params)
result = response.json()

# Extract the translated text
translated_text = result['translations'][0]['text']
print("Translated text:", translated_text)

# Ask the user if they want to save the translated text to a file
save_option = input("Do you want to save the translated text to a file? (yes/no): ").strip().lower()

if save_option == 'yes':
    file_name = input("Enter the file name (e.g., translation.txt): ").strip()
    with open(file_name, 'w') as file:
        file.write(translated_text)
    print(f"Translated text saved to {file_name}.")
else:
    print("Translated text not saved.")
