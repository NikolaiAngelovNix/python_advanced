from itertools import permutations


def possible_permutations(given_list):
    for el in permutations(given_list):
        yield list(el)
