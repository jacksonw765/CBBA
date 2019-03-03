import requests
import os
import csv
from datetime import datetime
from bs4 import BeautifulSoup

base_id = 39346
root_page = 'http://www.espn.com/mens-college-basketball/player/_/id/'
remainder = '/justin-jenifer?src=mobile'

for id in range(19, 20):
    request = root_page + str(base_id) + str(id) + remainder
    page = requests.get(request)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('h1')[0].getText()

    try:
        # check for invalid players
        if name != "College Basketball Players":
            #check if player is in NBA
            nba = soup.find("ul", "player-metadata floatleft").getText()
            if 'Drafted' not in nba:
                #history = soup.find_all("td", attrs={'style': 'text-align: right;'})[112].getText()
                #test = history.findAll(lambda tag: tag.name == 'td')

                team = soup.find("li", "last").getText()
                data = soup.find("table", "header-stats")
                PPG = data.findAll(lambda tag: tag.name == 'td')[0].getText()
                RPG = data.findAll(lambda tag: tag.name == 'td')[1].getText()
                APG = data.findAll(lambda tag: tag.name == 'td')[2].getText()
                print(name + ":")
                print(team)
                print(" PPG: " + PPG)
                print(" RPG: " + RPG)
                print(" APG: " + APG)

    except AttributeError as e:
        print("Player found but is bad" + str(e))

