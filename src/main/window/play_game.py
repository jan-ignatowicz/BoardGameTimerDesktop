# pylint: disable=R0902
"""Play game window"""
import time
from threading import Thread

from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.model.game import Game
from src.main.window.utils.player import Player
from src.resources.ui import play_game


class PlayGame(QWidget, play_game.Ui_Form):
    """
    Class is responsible for application play game window view.
    """

    def __init__(self, bgt_window, game_name, players_number):
        """
        Initializes a PlayGameWindow.

        :param bgt_window: main window view class.
        :param game_name: name of the actual playing game.
        :param players_number: number of players actual playing.
        """

        super().__init__()

        self.bgt_window = bgt_window

        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Board Game Timer - Play Game Window")

        self.game: Game = dao.get_game_by_name(game_name)
        self.players_number = int(players_number)

        self.setup_play_game_ui()

        self.endRoundButton.clicked.connect(self.end_round)
        self.passButton.clicked.connect(self.pass_tour)
        self.pauseButton.clicked.connect(self.pause_game)
        self.endGameButton.clicked.connect(self.end_game)

        self.actual_queue = []
        self.next_queue = []

        self.prepare_players_queue()
        self.update_players_queue_table_widget()

        self.actual_player: Player = self.get_actual_player()
        self.actual_play_thread = None
        self.semaphore = False
        self.actual_round_time_left = 0
        self.actual_game_time_left = 0
        self.update_actual_player_frame()

    def setup_play_game_ui(self):
        """
        Sets the view with received parameters from Main Window.

        :return:
        """

        self.gameNameLabel.setText(self.game.game_name)
        self.playersNumberInfoLabel.setText(str(self.players_number))
        self.roundTimeInfoLabel.setText(self.game.round_time)
        self.gameTimeInfoLabel.setText(self.game.game_time)
        self.pauseButton.setText("START")

    def clear_queue_table_widget(self):
        """
        Clears the queue table table in view before updating it.

        :return:
        """

        while self.playersQueueTableWidget.rowCount() > 0:
            self.playersQueueTableWidget.removeRow(0)

    def prepare_players_queue(self):
        """
        Prepares players while initializing a PlayGameWindow.

        :return:
        """

        self.actual_queue = []
        for i in range(self.players_number):
            name = "Player " + str(i + 1)
            player = Player(name, self.game.round_time, self.game.game_time)
            self.actual_queue.append(player)

    def get_actual_player(self):
        """
        Get first player from currently playing queue.

        :return: currently active player
        """

        return self.actual_queue[0]

    def update_view(self):
        """
        Updates the view after each action.

        :return:
        """

        self.update_players_queue_table_widget()
        self.update_actual_player_frame()

    def update_actual_player_frame(self):
        """
        Updates actual player frame after each second counting or after displaying new player.

        :return:
        """

        self.playerNameLabel.setText(self.actual_player.name)
        self.actualRoundTimeInfoLabel.setText(self.game.round_time)
        self.actualGameTimeInfoLabel.setText(self.actual_player.game_time)

        self.actualGameTimeInfoLabel.setDisabled(False)
        self.actualRoundTimeInfoLabel.setDisabled(False)

    def update_players_queue_table_widget(self):
        """
        Updates players queue table widget after actions like end round or pass.

        :return:
        """

        self.clear_queue_table_widget()
        for i, player in enumerate(self.actual_queue):
            self.playersQueueTableWidget.insertRow(i)
            self.playersQueueTableWidget.setItem(i, 0, QTableWidgetItem(player.name))
            self.playersQueueTableWidget.setItem(i, 1, QTableWidgetItem(player.game_time))

    def pause_game(self):
        """
        Pause the time counter.
        If game is paused, starts the counter.

        :return:
        """

        if self.pauseButton.text() == "START":
            self.semaphore = False
            self.pauseButton.setText("PAUSE")
            self.actual_play_thread = Thread(target=self.start_counting_time,
                                             args=(lambda: self.semaphore,))
            self.actual_play_thread.start()
        elif self.pauseButton.text() == "RESUME":
            self.semaphore = False
            self.pauseButton.setText("PAUSE")
            self.actual_play_thread = Thread(target=self.start_counting_time,
                                             args=(lambda: self.semaphore,))
            self.actual_play_thread.start()
        else:
            self.semaphore = True
            self.pauseButton.setText("RESUME")

    def get_time_left(self, mode):
        """
        Counts the player's time left in selected mode.

        :param mode: mode of the time, can be: round or game
        :return:
        """

        if mode == "round":
            self.actual_round_time_left = \
                60 * int(self.actual_player.actual_round_time[0:2]) + \
                int(self.actual_player.actual_round_time[3:])
            return self.actual_round_time_left

        self.actual_game_time_left = \
            60 * int(self.actual_player.game_time[0:2]) + int(self.actual_player.game_time[3:])
        return self.actual_game_time_left

    def start_counting_time(self, stop):
        """
        Starts counting time for actual player.

        :param stop: semaphore for stopping counting time on demand.
        :return:
        """

        mode = "round" if self.actual_player.actual_round_time != "00:00" else "game"

        time_left = self.get_time_left(mode)

        while time_left > 0:
            minutes, seconds = divmod(time_left, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)

            if mode == "round":
                self.actualRoundTimeInfoLabel.setText(timer)
            else:
                self.actualGameTimeInfoLabel.setText(timer)

            time.sleep(1)
            time_left -= 1

            if stop():
                if mode == "round":
                    self.actual_player.actual_round_time = timer
                else:
                    self.actual_player.game_time = timer
                self.actual_queue[0] = self.actual_player
                self.actual_play_thread = None
                return

        timer = "00:00"
        if mode == "round":
            self.actual_player.actual_round_time = timer
            self.actualRoundTimeInfoLabel.setText(timer)
            self.actualRoundTimeInfoLabel.setDisabled(True)
            self.start_counting_time(stop)
        else:
            self.actual_player.game_time = timer
            self.actualGameTimeInfoLabel.setText(timer)
            self.actualGameTimeInfoLabel.setDisabled(True)
            self.actual_queue[0] = self.actual_player
            print(f"{self.actual_player.name} time has gone")

        # QMessageBox.critical(self, "Time is gone!", f"Player: {self.actual_player.name} is
        # run out of game time!", QMessageBox.Ok)

    def end_round(self):
        """
        Ends the actual player round triggered by 'END ROUND' button.

        :return:
        """

        self.semaphore = True
        time.sleep(1)

        player = self.actual_player
        player.actual_round_time = self.game.round_time

        self.actual_queue.remove(self.actual_player)
        self.actual_queue.append(player)

        self.actual_player = self.actual_queue[0]

        self.update_view()
        self.pauseButton.setText("START")

    def pass_tour(self):
        """
        Passes the actual player tour triggered by 'PASS' button.

        :return:
        """

        self.semaphore = True
        time.sleep(1)

        player = self.actual_player
        player.actual_round_time = self.game.round_time

        self.actual_queue.remove(self.actual_player)
        self.next_queue.append(player)

        if not self.actual_queue:
            self.end_tour()
        else:
            self.actual_player = self.actual_queue[0]
            self.update_view()
            self.pauseButton.setText("START")

    def end_tour(self):
        """
        Ends game tour if all players passed their tours.

        :return:
        """

        self.actual_queue = self.next_queue
        self.next_queue = []
        self.actual_player = self.actual_queue[0]

        self.update_view()
        self.pauseButton.setText("START")

    def end_game(self):
        """
        Ends the game triggered by 'END GAME' button.

        :return:
        """

        self.semaphore = True
        self.actual_play_thread = None
        self.exit_window()

    def exit_window(self):
        """
        Exits the PlayGame window.

        :return:
        """

        PlayGame.close(self)
        self.bgt_window.show()
