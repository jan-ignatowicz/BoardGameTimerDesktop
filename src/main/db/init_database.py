"""Initializes database with 'games' table and example games."""
from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.model.game import Game
from src.main.exceptions.game_already_exists_exception import GameAlreadyExistsException


def example_games():
    """
    Provides three examples games.

    :return: list of three example games.
    """

    return [Game('Terra Mystica', '2', '5', '01:30', '30:00', 'queue'),
            Game('Terraformacja Marsa', '1', '5', '02:00', '15:00', 'queue'),
            Game('Cyklady', '2', '6', '01:40', '25:00', 'queue')]


def init_database():
    """
    Initializes database.
    Creates a 'games' table and add three examples games to database.

    :return:
    """

    dao.create_db_schema()
    games = example_games()

    for game in games:
        try:
            dao.add_game(game)
        except GameAlreadyExistsException:
            pass
