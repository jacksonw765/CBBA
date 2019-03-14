import sql_player
import bs4
import requests


def player_len(soup, id):
    try:
        year = soup.find('ul', 'general-info').find_all('li')[1].getText()
        base_index = 28
        base_log = soup.find_all("td", attrs={'style': 'text-align: right;'})
        if year == "Freshman":
            print("Freshman: " + str(id) + " " +str(base_log.__len__()))
        if year == "Sophomore":
            print("Sophmore: " + str(id) + " " +str(base_log.__len__()))
        if year == 'Junior':
            print("Junir: " + str(id) + " " +str(base_log.__len__()))
        if year == 'Senior':
            # check if 5th year
            if base_log.__len__() > 182:
                print("5th Year: " + str(id) + " " +str(base_log.__len__()))
            else:
                print("senior: " + str(id) + " " +str(base_log.__len__()))
    except Exception as ex:
        print("Woah big error: " + str(ex.__str__()))


root_page = 'http://www.espn.com/mens-college-basketball/player/_/id/'
remainder = '/justin-jenifer?src=mobile'

id_list = sql_player.get_ids()

for id in id_list:
    request = root_page + str(id) + remainder
    page = requests.get(request)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('h1')[0].getText()
    player_len(soup, id)


