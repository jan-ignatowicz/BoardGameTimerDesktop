import sys
import unittest

from PyQt5.QtWidgets import QApplication
from src.main.window.bgt_main import BgtMain

from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.model.game import Game

from src.main.exceptions.game_already_exists_exception import GameAlreadyExistsException
from src.main.exceptions.game_not_exist import GameNotExistException

app = QApplication(sys.argv)


class BgtMainTest(unittest.TestCase):

    def setUp(self):
        for game in dao.get_all_games():
            dao.delete_game_by_name(game.game_name)

        self.test_game = Game('Test game', '2', '5', '01:30', '30:00', 'queue')

    def add_test_game(self):
        try:
            dao.add_game(self.test_game)

        except GameAlreadyExistsException:
            print("Error while adding new game. Raised GameAlreadyExistsException!")

    def delete_test_game(self):
        dao.delete_game_by_name(self.test_game.game_name)

    def test__init__(self):
        self.bgt = BgtMain()

        assert self.bgt.isEnabled()
        assert self.bgt.addGameButton.text() == "ADD GAME"
        assert self.bgt.myGamesLabel.text() == "My games"
        assert self.bgt.playButton.text() == "PLAY"

    def test_update_games_list_view(self):
        self.add_test_game()
        self.bgt = BgtMain()

        self.bgt.update_games_list_view()
        games = [str(self.bgt.myGamesListWidget.item(i).text()) for i in
                 range(self.bgt.myGamesListWidget.count())]

        assert self.test_game.game_name in games

        self.delete_test_game()

    def test_show_game_quick_view(self):
        self.add_test_game()
        self.bgt = BgtMain()

        assert self.bgt.gameQuickViewFrame.isHidden()

        self.bgt.myGamesListWidget.setCurrentRow(0)
        self.bgt.show_game_quick_view()

        assert not self.bgt.gameQuickViewFrame.isHidden()

        self.delete_test_game()

    def test_open_add_game_window(self):
        self.bgt = BgtMain()

        assert self.bgt.isVisible()
        assert self.bgt.add_game_window is None

        self.bgt.open_add_game_window()

        assert not self.bgt.isVisible()
        assert self.bgt.add_game_window.isVisible()

    def test_open_edit_game_window(self):
        self.add_test_game()
        self.bgt = BgtMain()

        assert self.bgt.isVisible()
        assert self.bgt.edit_game_window is None

        self.bgt.myGamesListWidget.setCurrentRow(0)
        self.bgt.show_game_quick_view()

        self.bgt.open_edit_game_window()

        assert not self.bgt.isVisible()
        assert self.bgt.edit_game_window.isVisible()

        self.delete_test_game()

    def test_open_play_game_window(self):
        self.add_test_game()
        self.bgt = BgtMain()

        assert self.bgt.isVisible()
        assert self.bgt.play_game_window is None

        self.bgt.myGamesListWidget.setCurrentRow(0)
        self.bgt.show_game_quick_view()

        self.bgt.open_play_game_window()

        assert not self.bgt.isVisible()
        assert self.bgt.play_game_window.isVisible()

        self.delete_test_game()

    def test_delete_game(self):
        self.add_test_game()
        self.bgt = BgtMain()

        self.bgt.myGamesListWidget.setCurrentRow(0)
        self.bgt.show_game_quick_view()

        assert self.test_game.game_name == self.bgt.currently_selected_game
        assert dao.get_game_by_name(self.test_game.game_name) is not None

        self.bgt.delete_game()

        self.assertRaises(GameNotExistException, dao.get_game_by_name, self.test_game.game_name)

    def test_clear_main_view(self):
        self.add_test_game()
        self.bgt = BgtMain()

        assert self.bgt.myGamesListWidget.count() != 0

        self.bgt.clear_main_view()

        assert self.bgt.myGamesListWidget.count() == 0

        self.delete_test_game()
