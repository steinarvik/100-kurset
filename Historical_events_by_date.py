import requests

month = 8
day   = 15


url = f"https://history.muffinlabs.com/date/{month}/{day}"

response = requests.get(url)
data = response.json()

events = data['data'] ['Events']

##  grensesnittet ere endret, får ikke

for event in events:
    print(event['year'])
    print(event['text'])
    print(event['links'])