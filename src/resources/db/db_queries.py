"""GAME - CRUD queries"""

ADD_GAME = """
INSERT INTO games VALUES (:game_name, :min_players, :max_players, :round_time, :game_time, 
:game_type)
"""

GET_GAME_BY_NAME = """SELECT * FROM games WHERE game_name=:game_name"""

GET_ALL_GAMES = """SELECT * FROM games"""

UPDATE_GAME = """
    UPDATE games SET 
        min_players = :min_players, 
        max_players = :max_players, 
        round_time = :round_time, 
        game_time = :game_time, 
        game_type = :game_type
    WHERE game_name=:game_name
"""

DELETE_GAME = """DELETE FROM games WHERE game_name = :game_name"""
