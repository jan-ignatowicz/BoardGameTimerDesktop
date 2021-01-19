"""Database connection"""
import sqlite3

import src.resources.db.db_queries as q

import src.resources.application_settings as app_set
from src.main.exceptions.game_already_exists_exception import GameAlreadyExistsException
from src.main.exceptions.game_not_exist import GameNotExistException


class Database:
    """
    The sqlite3 database class.

    Also holds testers jobs.

    :param: __DB_LOCATION: store path to sqlite3 database file
    """

    __DB_LOCATION = app_set.db_path

    def __init__(self, *, db_location=None):
        """
        Initialize db class variables

        :param db_location: used only for testing, otherwise db_location i
        """

        if db_location is not None:
            self.db_location = db_location
        else:
            self.db_location = self.__DB_LOCATION

        self.connection = self.get_db_connection()
        self.cursor = self.get_cursor()

    def __enter__(self):
        """
        Override enter method.

        :return:
        """

        return self

    def __exit__(self, ext_type, exc_value, traceback):
        """
        Override exit method. Is called after each called method in this class.
        Commits or rollbacks transaction.
        Closes database connection.

        :param ext_type:
        :param exc_value:
        :param traceback:
        :return:
        """

        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def get_db_connection(self):
        """
        Getting db connection or raises db connection error.

        :return: db connection
        """

        try:
            return sqlite3.connect(self.db_location)
        except sqlite3.OperationalError as db_error:
            raise sqlite3.OperationalError from db_error

    def get_cursor(self):
        """
        Getting db cursor.

        :return: db cursor
        """

        return self.connection.cursor()

    def create_db_schema(self):
        """
        Creates table in database if not exists.
        Uses prepared sql script. Script is located in resources.

        :return:
        """

        with open(app_set.bgt_model_path) as bgt_model:
            self.connection.executescript(bgt_model.read())
            print("Schema successfully created!")

    def add_game(self, *, game_name, min_players, max_players, round_time, game_time, game_type):
        """
        Add game into games table.

        :param game_name: name of a game. This is a unique parameter. Not null.
        :param min_players: minimal number of players. Not null.
        :param max_players: maximal number of players. Not null.
        :param round_time: time for a round. Not null.
        :param game_time: time for a game. Not null.
        :param game_type: type of the game. Possible choices: queue.
        :return:
        """

        try:
            self.cursor.execute(q.ADD_GAME,
                                {'game_name': game_name,
                                 'min_players': min_players,
                                 'max_players': max_players,
                                 'round_time': round_time,
                                 'game_time': game_time,
                                 'game_type': game_type}
                                )

        except sqlite3.Error as sqlite_error:
            print(f"error: {sqlite_error}. Game of name \"{game_name}\" already exists!")
            raise GameAlreadyExistsException from sqlite_error

    def get_game_by_name(self, game_name):
        """
        Finds a game in database. Returns if positive, otherwise raises exception.

        :param game_name: name of searching game.
        :return: tuple of parameters of the found game.
        """

        try:
            self.cursor.execute(q.GET_GAME_BY_NAME, {'game_name': game_name})
            game = self.cursor.fetchone()

            assert game is not None

            return game

        except AssertionError as assertion_error:
            print(f"error: {assertion_error} Game of name \"{game_name}\" does not exist!")
            raise GameNotExistException from assertion_error

    def get_all_games(self):
        """
        Searches for all games.

        :return: list of parameters tuples of all games.
        """

        self.cursor.execute(q.GET_ALL_GAMES)

        games = self.cursor.fetchall()

        return games

    def update_game(self, *, game_name, min_players, max_players, round_time, game_time, game_type):
        """
        Updates game in games table.

        :param game_name: name of a game to update. This is a unique parameter. Not null.
        :param min_players: minimal number of players. Not null.
        :param max_players: maximal number of players. Not null.
        :param round_time: time for a round. Not null.
        :param game_time: time for a game. Not null.
        :param game_type: type of the game. Possible choices: queue.
        :return:
        """

        self.cursor.execute(q.UPDATE_GAME,
                            {'game_name': game_name,
                             'min_players': min_players,
                             'max_players': max_players,
                             'round_time': round_time,
                             'game_time': game_time,
                             'game_type': game_type}
                            )

    def delete_game_by_name(self, game_name):
        """
        Deletes game from games table.

        :param game_name: name of a game to delete. This is a unique parameter. Not null.
        :return:
        """

        self.cursor.execute(q.DELETE_GAME, {'game_name': game_name})
