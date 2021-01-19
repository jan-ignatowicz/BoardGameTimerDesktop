"""GameAlreadyExistsException"""


class GameAlreadyExistsException(Exception):
    """
    Provides new type for exception.

    This exception is thrown when user wants to add a new game with the already existing name.
    """
