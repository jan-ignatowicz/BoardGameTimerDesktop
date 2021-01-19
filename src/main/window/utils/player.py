"""Player helper class"""


class Player:
    """
    Helper class keeping info about players during playing a game.
    """

    def __init__(self, name, round_time, game_time):
        self.name = name
        self.actual_round_time = round_time
        self.game_time = game_time

    def __repr__(self):
        """
        Override method.

        :return:
        """

        return "Player('{}', '{}', '{}')".format(self.name, self.actual_round_time, self.game_time)

    def get_parameters(self):
        """
        Simplifies usage , mostly for database and testing.

        :return: tuple of model parameters.
        """

        return self.name, self.actual_round_time, self.game_time
