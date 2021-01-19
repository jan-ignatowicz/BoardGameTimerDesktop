"""Application main window"""
from PyQt5.QtWidgets import QWidget, QMessageBox

from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.model.game import Game
from src.main.exceptions import bad_manage_window_type
from src.main.window.manage_game import ManageGame
from src.main.window.play_game import PlayGame
from src.resources.ui import main


class BgtMain(QWidget, main.Ui_Form):
    """
    Class is responsible for application main window view.
    """

    def __init__(self):
        super().__init__()

        self.games = []
        self.currently_selected_game = None
        self.add_game_window = None
        self.edit_game_window = None
        self.play_game_window = None

        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Board Game Timer - Desktop Application")
        self.playerNameLabel.setText("Player1")
        self.playerNameLabel.hide()

        self.update_games_list_view()

        self.addGameButton.clicked.connect(self.open_add_game_window)

        self.exitButton.clicked.connect(self.exit_game)

    def update_games_list_view(self):
        """
        Updates 'My games' list view with actual games stored in database.

        :return:
        """

        self.clear_main_view()

        self.games = dao.get_all_games()

        self.myGamesListWidget.addItems(sorted([game.game_name for game in self.games]))

        self.myGamesListWidget.itemClicked.connect(self.show_game_quick_view)

    def show_game_quick_view(self):
        """
        Shows the preview of a game to play.

        :return:
        """

        self.currently_selected_game = self.myGamesListWidget.currentItem().text()
        game: Game = dao.get_game_by_name(self.currently_selected_game)

        self.gameNameLabel.setText(game.game_name)
        self.playersNumberSpinBox.setValue(int(game.min_players))
        self.playersNumberSpinBox.setMinimum(int(game.min_players))
        self.playersNumberSpinBox.setMaximum(int(game.max_players))
        self.roundTimeInfoLabel.setText(str(game.round_time))
        self.gameTimeInfoLabel.setText(str(game.game_time))
        self.gameQuickViewFrame.show()

        self.deleteGameButton.clicked.connect(self.delete_game_message)
        self.editGameButton.clicked.connect(self.open_edit_game_window)
        self.playButton.clicked.connect(self.open_play_game_window)
        self.playButton.show()

    def open_add_game_window(self):
        """
        Opens ManageGameWindow with type 'ADD'.

        :return:
        """

        self.add_game_window = ManageGame(self, "ADD")
        BgtMain.close(self)
        try:
            self.add_game_window.show()
        except bad_manage_window_type.BadManageWindowTypeException:
            print("Error while opening a manage window!")

    def open_edit_game_window(self):
        """
        Opens ManageGameWindow with type 'EDIT'.

        :return:
        """

        self.edit_game_window = ManageGame(self, "EDIT", game_name=self.currently_selected_game)
        BgtMain.close(self)
        try:
            self.edit_game_window.show()
        except bad_manage_window_type.BadManageWindowTypeException:
            print("Error while opening a manage window!")

    def open_play_game_window(self):
        """
        Opens PlayGameWindow.

        :return:
        """

        players_number = self.playersNumberSpinBox.text()
        self.play_game_window = PlayGame(self, self.currently_selected_game, players_number)
        BgtMain.close(self)
        self.play_game_window.show()

    def delete_game_message(self):
        """
        Shows confirmation dialog box.

        :return:
        """

        reply = QMessageBox.question(self, "Delete game.",
                                     f"Delete {self.currently_selected_game} from database?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.delete_game()

        # prevent showing QMessageBox twice
        self.deleteGameButton.disconnect()
        self.deleteGameButton.clicked.connect(self.delete_game_message)
        #

    def delete_game(self):
        """
        Sends delete requests with game name to delete.

        :return:
        """

        dao.delete_game_by_name(self.currently_selected_game)

        self.update_games_list_view()

    def clear_main_view(self):
        """
        Clears main view before initializing and showing it.

        :return:
        """

        self.myGamesListWidget.clear()
        self.currently_selected_game = None
        self.gameQuickViewFrame.hide()
        self.playButton.hide()

    def show(self):
        """
        Override method.
        After adding a game in Add Game Window, the my games list view must be updated.

        :return:
        """

        self.update_games_list_view()
        super().show()

    def exit_game(self):
        """
        Exits a game.
        Shows confirmation dialog box.

        :return:
        """

        reply = QMessageBox.question(self, "Exit.", "Do you want to exit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            BgtMain.close(self)
