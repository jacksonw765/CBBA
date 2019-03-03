import requests
import pprint
from bs4 import BeautifulSoup

base_id = 39346
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

for id in range(19, 25):
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
                year = soup.find('ul', 'general-info').find_all('li')[1].getText()
                base_index = 28
                base_log = soup.find_all("td", attrs={'style': 'text-align: right;'})
                print(name)
                game_list = []
                if year == "Freshman":
                    pprint.pprint(get_previous_game(base_log, base_index))
                    pprint.pprint(get_previous_game(base_log, base_index))
                if year == "Sophomore":
                    base_index = base_index * 2
                    pprint.pprint(get_previous_game(base_log, base_index))
                    pprint.pprint(get_previous_game(base_log, base_index+14))
                if year == 'Junior':
                    base_index = base_index*3
                    pprint.pprint(get_previous_game(base_log, base_index))
                    pprint.pprint(get_previous_game(base_log, base_index+14))
                if year == 'Senior':
                    base_index = base_index * 4
                    pprint.pprint(get_previous_game(base_log, base_index))
                    pprint.pprint(get_previous_game(base_log, base_index+14))



                """
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
                """

    except AttributeError as e:
        print("Player found but is bad" + str(e))





