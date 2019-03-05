import sqlite3


def create_sql_game_log(id, game, min, fg, e_point, reb, ast, blk, stl, turno, pts):
    con = sqlite3.connect('player_data.db')
    values = id, game, min, fg, e_point, reb, ast, blk, stl, turno, pts
    con.execute('INSERT INTO GameHistory VALUES (?,?,?,?,?,?,?,?,?,?,?)', values)
    con.commit()
    con.close()