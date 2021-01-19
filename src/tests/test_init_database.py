import unittest
from unittest.mock import MagicMock

from src.main.db.dao.game_dao import GameDao as dao

from src.main.db import init_database as init_db


class InitDatabaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.init_db = init_db

    def test_init_database(self):
        dao.create_db_schema = MagicMock()
        dao.add_game = MagicMock()

        self.init_db.init_database()

        dao.create_db_schema.assert_called_once()
        dao.add_game.assert_called()
