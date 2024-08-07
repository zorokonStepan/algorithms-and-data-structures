import math


def binary_search(sorted_array, looking_for):
    guess = math.floor(len(sorted_array) / 2)
    upper_bound = len(sorted_array)
    lower_bound = 0

    while abs(sorted_array[guess] - looking_for) > 0.0001:
        if sorted_array[guess] > looking_for:
            upper_bound = guess
            guess = math.floor((guess + lower_bound) / 2)

        if sorted_array[guess] < looking_for:
            lower_bound = guess
            guess = math.floor((guess + upper_bound) / 2)

    return guess
