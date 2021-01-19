import sys
import unittest
from unittest.mock import MagicMock

from PyQt5.QtWidgets import QApplication

from src.main.window.bgt_main import BgtMain
from src.main.window.manage_game import ManageGame

from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.model.game import Game


# app = QApplication(sys.argv)  # one time for all tests


class ManageGameTest(unittest.TestCase):

    def setUp(self):
        self.manage_game = ManageGame(MagicMock(), 'ADD')

        for game in dao.get_all_games():
            dao.delete_game_by_name(game.game_name)

        self.players_number = 5
        self.test_game = Game('Test game', '2', '5', '01:30', '30:00', 'queue')

    def test_add_game_setup_ui(self):
        add_game_type = ManageGame(MagicMock(), 'ADD', game_name=self.test_game.game_name)

        assert add_game_type.isEnabled()
        assert add_game_type.manageGameButton.text() == "ADD GAME"
        assert add_game_type.manageGameLabel.text() == "ADD GAME"
        assert add_game_type.cancelButton.text() == "CANCEL"

    def test_edit_game_setup_ui(self):
        dao.get_game_by_name = MagicMock(return_value=self.test_game)
        edit_game_type = ManageGame(MagicMock(), 'EDIT', game_name=self.test_game.game_name)

        assert edit_game_type.isEnabled()
        assert edit_game_type.manageGameButton.text() == "EDIT GAME"
        assert edit_game_type.manageGameLabel.text() == "EDIT GAME"
        assert edit_game_type.cancelButton.text() == "CANCEL"

        assert edit_game_type.gameNameLineEdit.text() == self.test_game.game_name
        assert edit_game_type.minPlayersSpinBox.text() == self.test_game.min_players
        assert edit_game_type.maxPlayersSpinBox.text() == self.test_game.max_players
        assert edit_game_type.roundTimeEdit.text() == self.test_game.round_time
        assert edit_game_type.gameTypeComboBox.currentText() == self.test_game.game_type

    def test_add_game(self):
        dao.add_game = MagicMock()
        self.manage_game.gather_data = MagicMock(return_value=self.test_game)

        self.manage_game.add_game()

        dao.add_game.assert_called_once_with(self.test_game)

    def test_update_game(self):
        dao.update_game = MagicMock()
        self.manage_game.gather_data = MagicMock(return_value=self.test_game)

        self.manage_game.update_game()

        dao.update_game.assert_called_once_with(self.test_game)

    def test_gather_data(self):
        self.manage_game.get_game_name = MagicMock(return_value=self.test_game.game_name)
        self.manage_game.get_min_players = MagicMock(return_value=self.test_game.min_players)
        self.manage_game.get_max_players = MagicMock(return_value=self.test_game.max_players)
        self.manage_game.get_round_time = MagicMock(return_value=self.test_game.round_time)
        self.manage_game.get_game_time = MagicMock(return_value=self.test_game.game_time)
        self.manage_game.get_game_type = MagicMock(return_value=self.test_game.game_type)

        game = self.manage_game.gather_data()

        assert str(game) == str(self.test_game)

    def test_get_game_name(self):
        self.manage_game.gameNameLineEdit.text = MagicMock(return_value=self.test_game.game_name)

        game_name = self.manage_game.get_game_name()

        assert game_name == self.test_game.game_name

    def test_get_min_players(self):
        self.manage_game.minPlayersSpinBox.text = MagicMock(
            return_value=int(self.test_game.min_players))

        min_players = int(self.manage_game.get_min_players())

        assert min_players == int(self.test_game.min_players)

    def test_get_max_players(self):
        self.manage_game.maxPlayersSpinBox.text = MagicMock(
            return_value=int(self.test_game.max_players))

        max_players = int(self.manage_game.get_max_players(int(self.test_game.min_players)))

        assert max_players == int(self.test_game.max_players)

    def test_get_round_time(self):
        self.manage_game.roundTimeEdit.text = MagicMock(return_value=self.test_game.round_time)

        round_time = self.manage_game.get_round_time()

        assert round_time == self.test_game.round_time

    def test_get_game_time(self):
        self.manage_game.gameTimeEdit.text = MagicMock(return_value=self.test_game.game_time)

        game_time = self.manage_game.get_game_time()

        assert game_time == self.test_game.game_time

    def test_get_game_type(self):
        self.manage_game.gameTypeComboBox.currentText = MagicMock(
            return_value=self.test_game.game_type)

        game_type = self.manage_game.get_game_type()

        assert game_type == self.test_game.game_type

    def test_exit_window(self):
        self.manage_game.bgt = BgtMain()

        self.manage_game.exit_window()

        assert self.manage_game.bgt.isVisible()
        assert self.manage_game.isHidden()

        self.manage_game.bgt = None
