EXPECTED_BAKE_TIME = 40 
PREPARATION_TIME = 2
print(EXPECTED_BAKE_TIME)
def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """Return preparation time, assuming each layer takes 2 minutes."""
    return PREPARATION_TIME * number_of_layers
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total elapsed cooking time."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time