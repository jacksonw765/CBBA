import bs4
import pprint
import requests
import sql_log

class GameLog:

    def __init__(self, id):
        self.id = id

    def get_previous_game(self, base_log, index):
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
            game.append(min)
            game.append(fg_percent)
            game.append(e_percent)
            game.append(reb)
            game.append(ast)
            game.append(blk)
            game.append(stl)
            game.append(turno)
            game.append(pts)
        return game

    def logPlayerGames(self, soup):

        year = soup.find('ul', 'general-info').find_all('li')[1].getText()
        base_index = 28
        base_log = soup.find_all("td", attrs={'style': 'text-align: right;'})
        game_list = []
        if year == "Freshman":
            game_one = self.get_previous_game(base_log, base_index)
            sql_log.create_sql_game_log(self.id, 1, game_one[0], game_one[1], game_one[2], game_one[3], game_one[4],
                                        game_one[5], game_one[6], game_one[7], game_one[8])
        if year == "Sophomore":
            base_index = base_index * 2
            game_one = self.get_previous_game(base_log, base_index)
            sql_log.create_sql_game_log(self.id, 1, game_one[0], game_one[1], game_one[2], game_one[3], game_one[4],
                                        game_one[5], game_one[6], game_one[7], game_one[8])
            #pprint.pprint(self.get_previous_game(base_log, base_index + 14))
        if year == 'Junior':
            base_index = base_index * 3
            game_one = self.get_previous_game(base_log, base_index)
            sql_log.create_sql_game_log(self.id, 1, game_one[0], game_one[1], game_one[2], game_one[3], game_one[4],
                                        game_one[5], game_one[6], game_one[7], game_one[8])
            #pprint.pprint(self.get_previous_game(base_log, base_index + 14))
        if year == 'Senior':
            base_index = base_index * 4
            game_one = self.get_previous_game(base_log, base_index)
            sql_log.create_sql_game_log(self.id, 1, game_one[0], game_one[1], game_one[2], game_one[3], game_one[4],
                                        game_one[5], game_one[6], game_one[7], game_one[8])
            #pprint.pprint(self.get_previous_game(base_log, base_index + 14))


base_id = 3934620
root_page = 'http://www.espn.com/mens-college-basketball/player/_/id/'
remainder = '/justin-jenifer?src=mobile'


for id in range(0, 1):

    player_id = str(base_id + id)
    request = root_page + player_id + remainder
    page = requests.get(request)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('h1')[0].getText()
    GameLog(player_id).logPlayerGames(soup)