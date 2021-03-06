import bs4
import requests
import sql_log
import sql_player


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

    # recursively checks if min is valid
    def validate_index(self, base_log, index):
        base_index = index
        if base_log.__len__() < index:
            base_index = 28
        try:
            min = int(base_log[base_index].getText())
            if min <= 35:
                return base_index
            else:
                return self.validate_index(base_log, base_index + 28)
        except IndexError:
            return base_index

    def log_games(self, base_log, base_index):
        try:
            game_one = self.get_previous_game(base_log, base_index)
            game_two = self.get_previous_game(base_log, base_index + 14)
            game_three = self.get_previous_game(base_log, base_index + 28)
            sql_log.create_sql_game_log(self.id, 1, game_one[0], game_one[1], game_one[2], game_one[3], game_one[4],
                                        game_one[5], game_one[6], game_one[7], game_one[8])
            sql_log.create_sql_game_log(self.id, 2, game_two[0], game_two[1], game_two[2], game_two[3], game_two[4],
                                        game_two[5], game_two[6], game_two[7], game_two[8])
            sql_log.create_sql_game_log(self.id, 3, game_three[0], game_three[1], game_three[2], game_three[3],
                                        game_three[4],
                                        game_three[5], game_three[6], game_three[7], game_three[8])
        except Exception as e:
            print("No stats found: " + e.__str__() + ": " + str(self.id))

    # this is a horrible way to do it but it works and I'm pressed for time
    def log_player_games(self, soup):
        try:
            year = soup.find('ul', 'general-info').find_all('li')[1].getText()
            base_index = 28
            base_log = soup.find_all("td", attrs={'style': 'text-align: right;'})
            if year == "Freshman":
                index = None
                if base_index > int(base_log.__len__()):
                    index = self.validate_index(base_log, base_index)
                else:
                    index = base_index
                self.log_games(base_log, index)
            if year == "Sophomore":
                base_index = base_index * 2
                index = None
                if base_index > int(base_log.__len__()):
                    index = self.validate_index(base_log, base_index)
                else:
                    index = base_index
                self.log_games(base_log, index)
            if year == 'Junior':
                base_index = base_index * 3
                index = None
                if base_index > int(base_log.__len__()):
                    index = self.validate_index(base_log, base_index)
                else:
                    index = base_index
                self.log_games(base_log, index)
            if year == 'Senior':
                # check if 5th year
                if base_log.__len__() > 182:
                    base_index = base_index * 5
                    index = None
                    if base_index > int(base_log.__len__()):
                        index = self.validate_index(base_log, base_index)
                    else:
                        index = base_index
                    self.log_games(base_log, index)
                else:
                    base_index = base_index * 4
                    index = None
                    if base_index > int(base_log.__len__()):
                        index = self.validate_index(base_log, base_index)
                    else:
                        index = base_index
                    self.log_games(base_log, index)
        except Exception as ex:
            print("Woah big error: " + str(self.id) + " " +ex.__str__())


root_page = 'http://www.espn.com/mens-college-basketball/player/_/id/'
remainder = '/justin-jenifer?src=mobile'

id_list = sql_player.get_ids()

for id in id_list:
    request = root_page + str(id) + remainder
    page = requests.get(request)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('h1')[0].getText()
    GameLog(id).log_player_games(soup)
    print("Player: " + name + ", ID: " + str(id) + " found")
