import requests
import pprint
import time
import datetime
from bs4 import BeautifulSoup
import sql_connect

base_id = 3777183
root_page = 'http://www.espn.com/mens-college-basketball/player/_/id/'
remainder = '/justin-jenifer?src=mobile'



first = datetime.datetime.now()
for id in range(45600, 2000000):
    player_id = str(base_id + id)
    request = root_page + player_id + remainder
    page = requests.get(request)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('h1')[0].getText()
    print("Checking player ID: " + player_id)
    try:
        # check for invalid players
        if name != "College Basketball Players":

            #check if player is in NBA
            nba = soup.find("ul", "player-metadata floatleft").getText()
            if 'Drafted' not in nba:
                team = soup.find("li", "last").getText()
                data = soup.find("table", "header-stats")
                ppg = data.findAll(lambda tag: tag.name == 'td')[0].getText()
                rpg = data.findAll(lambda tag: tag.name == 'td')[1].getText()
                apg = data.findAll(lambda tag: tag.name == 'td')[2].getText()
                print("Player found: " + name)
                sql_connect.create_sql_player(int(player_id), name, team, ppg, rpg, apg)

    except AttributeError as e:
        print("Player found but has no stats")

last = datetime.datetime.now()
print((last - first).min)





