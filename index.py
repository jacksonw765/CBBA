import requests
import pprint
import time
import datetime
from bs4 import BeautifulSoup
import sql_connect

base_id = 30000
root_page = 'http://www.espn.com/mens-college-basketball/player/_/id/'
remainder = '/justin-jenifer?src=mobile'


def get_previous_game(base_log, index):
    game = []
    if index >= base_log.__len__():
        print("Player is out for season or did not play \n")
    else:
        min = base_log[index].getText()
        fg_percent = base_log[index + 2].getText()
        e_percent = base_log[index + 4].getText()
        reb = base_log[index + 7].getText()
        ast = base_log[index + 8].getText()
        blk = base_log[index + 9].getText()
        stl = base_log[index + 10].getText()
        turno = base_log[index + 12].getText()
        pts = base_log[index + 13].getText()
        game.append("1st game min: " + min)
        game.append("1st game fg%: " + fg_percent)
        game.append("1st game 3point: " + e_percent)
        game.append("1st game reb:" + reb)
        game.append("1st game ast:" + ast)
        game.append("1st game blk:" + blk)
        game.append("1st game stl:" + stl)
        game.append("1st game to:" + turno)
        game.append("1st game reb:" + pts)
    return game

first = datetime.datetime.now()
for id in range(0, 5000):
    time.sleep(1)
    player_id = str(base_id) + str(id)
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





