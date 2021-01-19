# pylint: disable=C0103
"""Database communication between app and 'games' table."""
from src.main.db.database import Database
from src.main.db.model.game import Game
from src.main.exceptions.game_already_exists_exception import GameAlreadyExistsException
from src.main.exceptions.game_not_exist import GameNotExistException


class GameDao:
    """
    Implementation of Data Access Object design pattern.

    This class provides a communication between application and Database Class.

    Here comes the mapping table to object model.
    """

    @staticmethod
    def create_db_schema():
        """
        Calls Database method to create 'games' table.

        :return:
        """

        with Database() as db:
            db.create_db_schema()

    @staticmethod
    def add_game(game: Game):
        """
        Maps Game model to values and passes them to Database.add_game() method.

        :param game: game to add to database.
        :return:
        """

        (game_name, min_players, max_players, round_time, game_time,
         game_type) = game.get_parameters()

        try:
            with Database() as db:
                db.add_game(game_name=game_name, min_players=min_players, max_players=max_players,
                            round_time=round_time, game_time=game_time, game_type=game_type)
        except GameAlreadyExistsException as game_exists:
            raise GameAlreadyExistsException from game_exists

    @staticmethod
    def get_game_by_name(game_namee):
        """
        Gets tuple of parameters from Database.get_game_by_name() and maps them to Game model.

        :param game_namee: name of the searching game.
        :return: found game as Game object.
        """

        try:
            with Database() as db:
                game_values = db.get_game_by_name(game_namee)

        except GameNotExistException as game_not_exist:
            raise GameNotExistException from game_not_exist

        game_name, min_players, max_players, round_time, game_time, game_type = game_values

        game = Game(game_name, min_players, max_players, round_time, game_time, game_type)

        return game

    @staticmethod
    def get_all_games():
        """
        Gets tuples of parameters from Database.get_all_games() and maps them to Game models.

        :return: all games stored in database, mapped to Game objects.
        """

        with Database() as db:
            games_tuples = db.get_all_games()

        games = []

        for game_tuple in games_tuples:
            game_name, min_players, max_players, round_time, game_time, game_type = game_tuple

            games.append(Game(game_name, min_players, max_players, round_time, game_time,
                              game_type))

        return games

    @staticmethod
    def update_game(game: Game):
        """
        Maps Game model to values and passes them to Database.update_game() method.

        :param game: game to update to database.
        :return:
        """

        (game_name, min_players, max_players, round_time, game_time,
         game_type) = game.get_parameters()

        with Database() as db:
            db.update_game(game_name=game_name, min_players=min_players, max_players=max_players,
                           round_time=round_time, game_time=game_time, game_type=game_type)

    @staticmethod
    def delete_game_by_name(game_name):
        """
        Pass delete game request to Database.delete_game_by_name()

        :param game_name: name of a game to delete.
        :return:
        """
        with Database() as db:
            db.delete_game_by_name(game_name)
