import requests
from bs4 import BeautifulSoup

url = 'https://gamenation.in/Search?term=ghost+of+tsushima&PS4=on&PS5=on&Sort=Relevance&TypeGames=on&ConditionPreOwned=on'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ProductListing")

games = results.find_all("div", class_="game-card")

for game in games:
    print("\n")
    title = game.find("div", class_="title")
    priceDiv = game.find("div", class_="pricing")
    price = priceDiv.find("b")
    print(title.text.strip())
    print(price.text.strip())
# print(games)


