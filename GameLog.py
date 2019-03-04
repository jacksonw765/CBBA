""""
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