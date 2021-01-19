# pylint: disable=R0913
"""Provides model of 'games' table."""


class Game:
    """
    Model of the game as table stored in database.
    """

    def __init__(self, game_name, min_players, max_players, round_time, game_time, game_type):
        """

        :param game_name: name of a game. This is a unique parameter. Not null.
        :param min_players: minimal number of players. Not null.
        :param max_players: maximal number of players. Not null.
        :param round_time: time for a round. Not null.
        :param game_time: time for a game. Not null.
        :param game_type: type of the game. Possible choices: queue.
        """

        self.game_name = game_name
        self.min_players = min_players
        self.max_players = max_players
        self.round_time = round_time
        self.game_time = game_time
        self.game_type = game_type

    def __repr__(self):
        """
        Override method.

        :return:
        """

        return "Game('{}', '{}', '{}', '{}', '{}', '{}')" \
            .format(self.game_name, self.min_players, self.max_players,
                    self.round_time, self.game_time, self.game_type)

    def get_parameters(self):
        """
        Simplifies usage , mostly for database and testing.

        :return: tuple of model parameters.
        """
        return (self.game_name, self.min_players, self.max_players,
                self.round_time, self.game_time, self.game_type)
