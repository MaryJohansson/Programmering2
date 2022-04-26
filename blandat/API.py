import requests

# In this uppgift you are supposed to fill in the spots where it says xxx or the rows with TODO
# Take the https address and open it in your browser to see the API content

# Uppgift 1
import requests as requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
answer = response.json()
print(f"One bitcoin is worth {answer['bpi']['USD']['rate']} EUR right now.")

# Uppgift 2

response = requests.get("https://open.er-api.com/v6/latest/USD")
answer = response.json()
print(f"One USD is worth {answer['rates']['SEK']} SEK right now.")

# Uppgift 3

response = requests.get("https://randomuser.me/api/")
answer = response.json()
print(
    f"Your agent name is {(''.join(answer['results'][0]['name'].values()))} and you live in {answer['results'][0]

and you live in {answer['results'][0]['location']['country']}")

# Uppgift 4

response = requests.get("https://date.nager.at/api/v2/publicholidays/2020/US")
answer = response.json()
print(f"The big holidays in the US are:")
for holiday in answer["holidays"]:
    print(holiday["date"], ":", holiday["localName"])

# TODO - Print out all holidays from answer. You will need a for loop.

# Uppgift 5

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=mojito")
answer = response.json()
print(f"The different mojito drinks I can offer is:")
for drink in answer["drinks"]:
    print(drink["idDrink"], ":", drink["strDrink"])

# TODO - Print out all mojito drinks from answer. You will need a for loop.
