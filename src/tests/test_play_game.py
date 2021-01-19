import sys
import unittest
from threading import Thread
from unittest.mock import MagicMock

from PyQt5.QtWidgets import QApplication

from src.main.window.bgt_main import BgtMain
from src.main.window.play_game import PlayGame

from src.main.db.dao.game_dao import GameDao as dao
from src.main.db.model.game import Game
from src.main.window.utils.player import Player


# app = QApplication(sys.argv)  # one time for all tests


class PlayGameTest(unittest.TestCase):

    def setUp(self):
        self.test_game = Game('Test game', '2', '5', '01:30', '30:00', 'queue')
        self.actual_player = Player('Player1', '01:45', '20:00')

        dao.get_game_by_name = MagicMock(return_value=self.test_game)
        PlayGame.get_actual_player = MagicMock(return_value=self.actual_player)

        self.play_game = PlayGame(MagicMock(), self.test_game.game_name, self.test_game.max_players)

    def test__init__(self):
        assert self.play_game.isEnabled()

    def test_setup_ui(self):
        assert self.play_game.gameNameLabel.text() == self.test_game.game_name
        assert self.play_game.playersNumberInfoLabel.text() == self.test_game.max_players
        assert self.play_game.roundTimeInfoLabel.text() == self.test_game.round_time
        assert self.play_game.gameTimeInfoLabel.text() == self.test_game.game_time
        assert self.play_game.pauseButton.text() == "START"

    def test_prepare_players_queue(self):
        self.play_game.players_number = 2

        self.play_game.prepare_players_queue()

        assert len(self.play_game.actual_queue) == 2

    def test_get_actual_player(self):
        self.play_game.actual_queue = []
        self.play_game.actual_queue.append(self.actual_player)

        player = self.play_game.get_actual_player()

        assert str(player) == str(self.actual_player)

    def test_update_view(self):
        self.play_game.update_players_queue_table_widget = MagicMock()
        self.play_game.update_actual_player_frame = MagicMock()

        self.play_game.update_view()

        self.play_game.update_players_queue_table_widget.assert_called_once()
        self.play_game.update_actual_player_frame.assert_called_once()

    def test_update_players_queue_table_widget(self):
        self.play_game.actual_queue = [self.actual_player]

        self.play_game.update_players_queue_table_widget()

        assert self.play_game.playersQueueTableWidget.rowCount() > 0
        assert self.play_game.playersQueueTableWidget.item(0, 0).text() == self.actual_player.name

    def test_update_actual_player_frame(self):
        self.play_game.update_actual_player_frame()

        assert self.play_game.playerNameLabel.text() == self.actual_player.name
        assert self.play_game.actualRoundTimeInfoLabel.text() == self.test_game.round_time
        assert self.play_game.actualGameTimeInfoLabel.text() == self.actual_player.game_time

        assert self.play_game.actualGameTimeInfoLabel.isEnabled()
        assert self.play_game.actualRoundTimeInfoLabel.isEnabled()

    def test_pause_game_pause_mode(self):
        Thread.start = MagicMock()
        self.play_game.pauseButton.setText("PAUSE")

        self.play_game.pause_game()

        assert self.play_game.pauseButton.text() == "RESUME"

    def test_pause_game_start_mode(self):
        Thread.start = MagicMock()
        self.play_game.pauseButton.setText("START")

        self.play_game.pause_game()

        assert self.play_game.pauseButton.text() == "PAUSE"

    def test_pause_game_resume_mode(self):
        Thread.start = MagicMock()
        self.play_game.pauseButton.setText("RESUME")

        self.play_game.pause_game()

        assert self.play_game.pauseButton.text() == "PAUSE"

    def test_get_time_left_round_time_mode(self):
        self.actual_player.actual_round_time = "01:30"

        round_time_left = self.play_game.get_time_left('round')

        assert round_time_left == 90

    def test_get_time_left_game_time_mode(self):
        self.actual_player.game_time = "30:00"

        game_time_left = self.play_game.get_time_left('game')

        assert game_time_left == 1800

    def test_start_counting_time(self):
        self.play_game.get_time_left = MagicMock(return_value=1)
        self.play_game.actual_player.actual_round_time = "00:01"

        self.play_game.start_counting_time(MagicMock(return_value=False))

        assert self.play_game.actualRoundTimeInfoLabel.text() == "00:00"

    def test_end_round(self):
        player2 = self.actual_player
        player2.name = "Player2"

        self.play_game.actual_queue = [self.actual_player, player2]

        self.play_game.end_round()

        assert self.play_game.actual_player.name == player2.name
        assert self.play_game.actual_queue[0].name == player2.name
        assert self.play_game.pauseButton.text() == "START"

    def test_pass_tour(self):
        player2 = self.actual_player
        player2.name = "Player2"

        self.play_game.actual_queue = [self.actual_player, player2]
        self.play_game.next_queue = []

        self.play_game.pass_tour()

        assert self.play_game.actual_player.name == player2.name
        assert self.play_game.actual_queue[0].name == player2.name
        assert self.play_game.pauseButton.text() == "START"

        assert self.play_game.next_queue[0].name == self.actual_player.name

    def test_end_game(self):
        self.play_game.exit_window = MagicMock()

        self.play_game.end_game()

        assert self.play_game.semaphore == True

    def test_exit_game(self):
        self.play_game.bgt_window = BgtMain()

        self.play_game.exit_window()

        assert self.play_game.bgt_window.isEnabled()
        assert self.play_game.isHidden()
