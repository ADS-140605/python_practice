"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): elapsed baking time.

    Returns:
        int: remaining baking time.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    Parameters:
        number_of_layers (int): number of lasagna layers.

    Returns:
        int: preparation time in minutes.
    """

    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time.

    Parameters:
        number_of_layers (int): number of layers.
        elapsed_bake_time (int): elapsed baking time.

    Returns:
        int: total elapsed time in minutes.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time