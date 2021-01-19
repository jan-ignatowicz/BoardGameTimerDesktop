"""Manage Game Window"""

from datetime import datetime
from PyQt5.QtWidgets import QWidget, QMessageBox

from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.model.game import Game
from src.main.exceptions import bad_manage_window_type, gather_data_exception, \
    game_already_exists_exception, incorrect_data_exception
from src.resources.ui import manage_game


class ManageGame(QWidget, manage_game.Ui_Form):
    """
    Class is responsible for application manage game window view.
    Makes it possible to add or edit a game.
    """

    def __init__(self, bgt_window, window_type, *, game_name=None):
        """
        Initializes a ManageGameWindow.

        :param bgt_window: main window view class.
        :param window_type: type of window to show; possible: 'ADD', 'EDIT'.
        :param game_name: name of the game to edit; available in 'EDIT' window_type.
        """

        super().__init__()

        self.bgt_window = bgt_window

        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Board Game Timer - Manage Game Window")

        if window_type == "ADD":
            self.add_game_setup_ui()
        elif window_type == "EDIT":
            self.edit_game_setup_ui(game_name)
        else:
            raise bad_manage_window_type.BadManageWindowTypeException

        self.cancelButton.clicked.connect(self.cancel)

    def add_game_setup_ui(self):
        """
        Setup ui for 'ADD' window type.

        :return:
        """

        self.manageGameLabel.setText("ADD GAME")
        self.manageGameButton.setText("ADD GAME")
        self.manageGameButton.clicked.connect(self.add_game)

    def edit_game_setup_ui(self, game_name):
        """
        Setup ui for 'EDIT' window type.

        :param game_name:
        :return:
        """

        game: Game = dao.get_game_by_name(game_name)

        self.gameNameLineEdit.setText(game_name)
        self.gameNameLineEdit.setDisabled(True)
        self.minPlayersSpinBox.setValue(int(game.min_players))
        self.maxPlayersSpinBox.setValue(int(game.max_players))
        self.roundTimeEdit.setTime(datetime.strptime(game.round_time, '%M:%S').time())
        self.gameTimeEdit.setTime(datetime.strptime(game.game_time, '%M:%S').time())
        self.gameTypeComboBox.setCurrentText(game.game_type)

        self.manageGameLabel.setText("EDIT GAME")
        self.manageGameButton.setText("EDIT GAME")
        self.manageGameButton.clicked.connect(self.update_game)

    def add_game(self):
        """
        Pass request to dao for adding currently defined game.

        :return:
        """

        try:
            game = self.gather_data()

            dao.add_game(game)

            self.exit_window()

        except gather_data_exception.GatherDataException:
            print("Error while adding new game. Raised GatherDataException!")
        except game_already_exists_exception.GameAlreadyExistsException:
            print("Error while adding new game. Raised GameAlreadyExistsException!")
            self.show_incorrect_data_message_box("Game of that name already exists. Choose another "
                                                 "name of the game or edit the existing one")

    def update_game(self):
        """
        Pass request to dao for updating currently defined game.

        :return:
        """

        try:
            game = self.gather_data()

            dao.update_game(game)

            self.exit_window()

        except gather_data_exception.GatherDataException:
            print("Error while editing a game. Raised GatherDataException!")

    def gather_data(self) -> Game:
        """
        Gathers data currently set in ui form.

        :return: gathered data mapped to Game object.
        """

        try:
            game_name = self.get_game_name()
            min_players = self.get_min_players()
            max_players = self.get_max_players(min_players)
            round_time = self.get_round_time()
            game_time = self.get_game_time()
            game_type = self.get_game_type()
        except incorrect_data_exception.IncorrectDataException as inc_data:
            print("Raised an IncorrectDataException!")
            raise gather_data_exception.GatherDataException from inc_data

        game = Game(game_name, min_players, max_players, round_time, game_time, game_type)

        return game

    def get_game_name(self):
        """
        Gather currently set game name in ui form.

        :return: got game name
        """

        game_name = self.gameNameLineEdit.text()

        reply = None
        if not isinstance(game_name, str):
            reply = self.show_incorrect_data_message_box("Name of a game should be a string.")
        elif len(game_name) < 1:
            reply = self.show_incorrect_data_message_box("Name of a game cannot be empty.")

        if reply == QMessageBox.Ok:
            raise incorrect_data_exception.IncorrectDataException

        return game_name

    def get_min_players(self):
        """
        Gather currently set minimum number of players in ui form.

        :return: got min players value
        """

        min_players = int(self.minPlayersSpinBox.text())
        return min_players

    def get_max_players(self, min_players):
        """
        Gather currently set maximum number of players in ui form.

        :param min_players: use to assert max players number higher than min players number
        :return: got max players value
        """

        max_players = int(self.maxPlayersSpinBox.text())

        reply = None
        if max_players < min_players:
            reply = self.show_incorrect_data_message_box("Number of max players must be higher than"
                                                         " a number of min players")

        if reply == QMessageBox.Ok:
            raise incorrect_data_exception.IncorrectDataException

        return max_players

    def get_round_time(self):
        """
        Gather currently set round time in ui form.

        :return: got round time
        """

        round_time = self.roundTimeEdit.text()
        return round_time

    def get_game_time(self):
        """
        Gather currently set game time in ui form.

        :return: got game time
        """

        game_time = self.gameTimeEdit.text()
        return game_time

    def get_game_type(self):
        """
        Gather currently set game type in ui form.

        :return: got game type
        """

        game_type = self.gameTypeComboBox.currentText()
        return game_type

    def show_incorrect_data_message_box(self, message):
        """
        Opens dialog box informing about incorrect provided data.

        :param message: message to show
        :return:
        """

        return QMessageBox.critical(self, "Incorrect data provided.", message, QMessageBox.Ok)

    def cancel(self):
        """
        Returns to Main Window.

        :return:
        """

        self.exit_window()

    def exit_window(self):
        """
        Exits currently window.

        :return:
        """

        ManageGame.close(self)
        self.bgt_window.show()
