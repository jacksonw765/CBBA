import sqlite3


def create_sql_player(id, name, team, ppp, rpg, apg):
    con = sqlite3.connect('player_data.db')
    values = id, name, team, ppp, rpg, apg
    con.execute('INSERT INTO Player VALUES (?,?,?,?,?,?)', values)
    con.commit()
    con.close()
