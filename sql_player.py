import sqlite3
import math

def create_sql_player(id, name, team, ppp, rpg, apg):
    try:
        con = sqlite3.connect('player_data.db')
        values = id, name, team, ppp, rpg, apg
        con.execute('INSERT INTO Player VALUES (?,?,?,?,?,?)', values)
        con.commit()
        con.close()
    except sqlite3.OperationalError as oe:
        print("Error running query: " + oe.__str__())


def get_team_total_ppg(team_name):
    try:
        con = sqlite3.connect('player_data.db')
        query = 'SELECT SUM(PPG) FROM Player WHERE Team = ' + '"' + team_name + '"'
        result = con.execute(query)
        value = result.fetchone()[0]
        con.close()
        return round(value, 2)
    except sqlite3.OperationalError as oe:
        print("Error running query PPG: " + oe.__str__())


def get_team_total_rpg(team_name):
    try:
        con = sqlite3.connect('player_data.db')
        query = 'SELECT SUM(RPG) FROM Player WHERE Team = ' + '"' + team_name + '"'
        result = con.execute(query)
        value = result.fetchone()[0]
        con.close()
        return round(value, 2)
    except sqlite3.OperationalError as oe:
        print("Error running query RPG: " + oe.__str__())


def get_team_total_apg(team_name):
    try:
        con = sqlite3.connect('player_data.db')
        query = 'SELECT SUM(ASP) FROM Player WHERE Team = ' + '"' + team_name + '"'
        result = con.execute(query)
        value = result.fetchone()[0]
        con.close()
        return round(value, 2)
    except sqlite3.OperationalError as oe:
        print("Error running query APG: " + oe.__str__())

def get_ids():
    try:
        con = sqlite3.connect('player_data.db')
        con.row_factory = lambda cursor, row: row[0]
        query = 'SELECT ID FROM Player'
        result = con.execute(query)
        value = result.fetchall()
        con.close()
        return list(value)
    except sqlite3.OperationalError as oe:
        print("Error running query APG: " + oe.__str__())
