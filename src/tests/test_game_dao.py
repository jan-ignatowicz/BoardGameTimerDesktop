import unittest
from unittest.mock import MagicMock

from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.database import Database
from src.main.db.model.game import Game


class DatabaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.dao = dao

        self.test_game = Game('Test game', '2', '5', '01:30', '30:00', 'queue')

        Database.get_db_connection = MagicMock()

    def test_create_db_schema(self):
        Database.create_db_schema = MagicMock()

        self.dao.create_db_schema()

        Database.create_db_schema.assert_called_once()

    def test_add_game(self):
        Database.add_game = MagicMock()
        (game_name, min_players, max_players, round_time, game_time,
         game_type) = self.test_game.get_parameters()

        self.dao.add_game(self.test_game)

        Database.add_game.assert_called_once_with(game_name=game_name, min_players=min_players,
                                                  max_players=max_players, round_time=round_time,
                                                  game_time=game_time, game_type=game_type)

    def test_get_game_by_name(self):
        Database.get_game_by_name = MagicMock(return_value=self.test_game.get_parameters())

        game = self.dao.get_game_by_name(self.test_game.game_name)

        Database.get_game_by_name.assert_called_once_with(self.test_game.game_name)

        self.assertIsInstance(game, Game)

    def test_get_game_by_name_game_not_exist(self):
        Database.get_game_by_name = MagicMock(return_value=None)

        with self.assertRaises(Exception):
            self.dao.get_game_by_name(self.test_game.game_name)

        Database.get_game_by_name.assert_called_once_with(self.test_game.game_name)

    def test_get_all_games(self):
        Database.get_all_games = MagicMock(
            return_value=[self.test_game.get_parameters(), self.test_game.get_parameters()])

        games = self.dao.get_all_games()

        Database.get_all_games.assert_called_once()

        assert len(games) == 2

    def test_update_game(self):
        Database.update_game = MagicMock()

        (game_name, min_players, max_players, round_time, game_time,
         game_type) = self.test_game.get_parameters()

        self.dao.update_game(self.test_game)

        Database.update_game.assert_called_once_with(game_name=game_name, min_players=min_players,
                                                     max_players=max_players, round_time=round_time,
                                                     game_time=game_time, game_type=game_type)

    def test_delete_game_by_name(self):
        Database.delete_game_by_name = MagicMock(return_value=self.test_game.get_parameters())

        self.dao.delete_game_by_name(self.test_game.game_name)

        Database.delete_game_by_name(self.test_game.game_name)
