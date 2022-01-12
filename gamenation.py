import requests
from bs4 import BeautifulSoup

def gamenation(name, isPS5, isPS4, isPreOwned, isNew):
    url = f'https://gamenation.in/Search?term={name}&Sort=Relevance&TypeGames=on'
    if isPS5:
        url+='&PS5=on'
    if isPS4:
        url+='&PS4=on'
    if isPreOwned:
        url+='ConditionPreOwned=on'
    if isNew:
        url+='ConditionNew=on'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    games = soup.find_all("a", class_='game-card-link')
    toReturn = []


    for game in games:
        available = game.find("div", class_="game-card un-available")
        gameUrl = game['href']
        if available!=None:
            continue
        title = game.find("div", class_="title")
        priceDiv = game.find("div", class_="pricing")
        price = priceDiv.find("b")
        gameDict = {
            'title' : title.text.strip(),
            'price' : price.text.strip(),
            'gameUrl' : gameUrl
        }
        toReturn.append(gameDict)
    return toReturn    

# name = 'ghost of tsushima'
# isPS5 = True
# isPS4 = True
# isNew = True
# isPreOwned = True

# print(gamenation(name,isPS5, isPS4, isPreOwned, isNew))


