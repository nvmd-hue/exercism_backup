"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 20


def bake_time_remaining(elapsed_bake_time: int | None = None):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)


def preparation_time_in_minutes(number_of_layers: int | None = None):
    """Calculate the preparation time in minutes
    
    Parameters:
        number_of_layers (int): How many layers to the lasagna.

    Returns:
        int: total preparation time (in minutes) derived from total layers
        and time for each layer

    """
    time_for_each_layer = 2
    return number_of_layers * time_for_each_layer


def elapsed_time_in_minutes(number_of_layers: int | None = None, elapsed_bake_time:int | None = None):
    """Calculate the total elasped time in minutes.

    Parameters:
        number_of_layers (int): How many laters to the lasagna.
        elapsed_bake_time (int): The baking time already elasped.

    Returns:
        int: total elapsed time of prep plus baking time    
    """
    return (preparation_time_in_minutes(number_of_layers) + elapsed_bake_time)
