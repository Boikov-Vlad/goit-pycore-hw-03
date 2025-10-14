import random

def get_numbers_ticket(min_value: int, max_value:int, quantity:int) -> list[int]:
    return_value = []

    if not all(type(x) is int for x in (min_value, max_value, quantity)):
        return return_value

    if min_value < 1 or max_value > 1000 or min_value > max_value:
        return return_value
    
    quantity_range_size = max_value - min_value + 1
    if not (1 <= quantity <= quantity_range_size):
        return return_value
    
    return_value = sorted(random.sample(range(min_value, max_value + 1), k=quantity))

    return return_value