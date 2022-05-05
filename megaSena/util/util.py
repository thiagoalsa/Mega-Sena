import random


def raffle(number_of_numbers, game_size):
    numbers_drawn = random.sample(range(1, game_size + 1), number_of_numbers)
    return sorted(numbers_drawn)



