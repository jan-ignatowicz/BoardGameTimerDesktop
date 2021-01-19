import sqlite3
import unittest
from unittest.mock import patch, MagicMock, Mock

from src.main.db.database import Database

from src.resources.db import db_queries as q

import src.resources.application_settings as app_set


class DatabaseTest(unittest.TestCase):

    @patch('sqlite3.connect')
    def setUp(self, mock_sql) -> None:
        self.mock_sql = mock_sql
        self.db = Database(db_location="test_database")

        self.game_values = 'Test game', '2', '5', '01:30', '30:00', 'queue'
        (self.game_name, self.min_players, self.max_players, self.round_time, self.game_time,
         self.game_type) = self.game_values

    def test_sqlite3_connect_success(self):
        sqlite3.connect = MagicMock(return_value='connection succeeded')
        Database.get_cursor = MagicMock()

        db = Database(db_location="test_database")

        sqlite3.connect.assert_called_with('test_database')
        self.assertEqual(db.connection, 'connection succeeded')

    def test_sqlite3_connect_fail(self):
        sqlite3.connect = MagicMock(return_value='connection failed')
        Database.get_cursor = MagicMock()

        db = Database(db_location="test_database")

        sqlite3.connect.assert_called_with('test_database')
        self.assertEqual(db.connection, 'connection failed')

    def test_sqlite3_connect_with_side_affect(self):
        self._setup_mock_sqlite3_connect()

        db = Database(db_location='good_connection_string')
        self.assertTrue(db.connection)
        sqlite3.connect.assert_called_with('good_connection_string')

        db = Database(db_location='bad_connection_string')
        self.assertFalse(db.connection)
        sqlite3.connect.assert_called_with('bad_connection_string')

    @staticmethod
    def _setup_mock_sqlite3_connect():
        values = {'good_connection_string': True,
                  'bad_connection_string': False}

        def side_effect(arg):
            return values[arg]

        sqlite3.connect = Mock(side_effect=side_effect)

    def test_create_db_schema(self):
        self.db.connection.executescript = MagicMock()

        self.db.create_db_schema()

        with open(app_set.bgt_model_path) as bgt_model:
            self.db.connection.executescript.assert_called_once_with(bgt_model.read())

    def test_add_game(self):
        self.db.cursor.execute = MagicMock()

        self.db.add_game(game_name=self.game_name, min_players=self.min_players,
                         max_players=self.max_players, round_time=self.round_time,
                         game_time=self.game_time, game_type=self.game_type)

        self.db.cursor.execute.assert_called_once_with(q.ADD_GAME,
                                                       {'game_name': self.game_name,
                                                        'min_players': self.min_players,
                                                        'max_players': self.max_players,
                                                        'round_time': self.round_time,
                                                        'game_time': self.game_time,
                                                        'game_type': self.game_type}
                                                       )

    def test_get_game_by_name(self):
        self.db.cursor.execute = MagicMock()
        self.db.cursor.fetchone = MagicMock(return_value=self.game_values)

        game = self.db.get_game_by_name(self.game_name)

        self.db.cursor.execute.assert_called_once_with(q.GET_GAME_BY_NAME,
                                                       {'game_name': self.game_name})

        assert len(game) == 6

    def test_get_game_by_name_game_not_exist(self):
        self.db.cursor.execute = MagicMock(return_value=None)
        self.db.cursor.fetchone = MagicMock(return_value=None)

        with self.assertRaises(Exception):
            self.db.get_game_by_name(self.game_name)

        self.db.cursor.execute.assert_called_once_with(q.GET_GAME_BY_NAME,
                                                       {'game_name': self.game_name})

    def test_get_all_games(self):
        self.db.cursor.execute = MagicMock()
        self.db.cursor.fetchall = MagicMock(return_value=[self.game_values, self.game_values])

        self.db.get_all_games()

        self.db.cursor.execute.assert_called_once_with(q.GET_ALL_GAMES)

    def test_update_game(self):
        self.db.cursor.execute = MagicMock()

        self.db.update_game(game_name=self.game_name, min_players=self.min_players,
                            max_players=self.max_players, round_time=self.round_time,
                            game_time=self.game_time, game_type=self.game_type)

        self.db.cursor.execute.assert_called_once_with(q.UPDATE_GAME,
                                                       {'game_name': self.game_name,
                                                        'min_players': self.min_players,
                                                        'max_players': self.max_players,
                                                        'round_time': self.round_time,
                                                        'game_time': self.game_time,
                                                        'game_type': self.game_type}
                                                       )

    def test_delete_game_by_name(self):
        self.db.cursor.execute = MagicMock()

        self.db.delete_game_by_name(self.game_name)

        self.db.cursor.execute.assert_called_once_with(q.DELETE_GAME,
                                                       {'game_name': self.game_name})
