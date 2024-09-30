import requests

country = 'Norway'

url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)

data = response.json()


capitals = data[0]['capital']
region = data[0]['region']
population = data[0]['population']
languages = data[0]['languages']['nno']
for capital in capitals:
    print(capital)
print(region)
print(population)
for language in languages:
    print(language)
