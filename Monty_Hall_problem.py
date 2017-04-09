#!/usr/bin/env python3.6
import random


def draw_lots(size: int = 100, left_closed: int = 2) -> bool:
    """For number of gates specified in size parameter selects random winning gate and player's selection.
    Then, makes simulation to prove that Monty Hall is right."""

    winning = round((size - 1) * random.random()) + 1
    selection = round((size - 1) * random.random()) + 1

    gates = [0] * size
    gates[winning - 1] = 1000

    # left left_empty gates closed
    for i in range((size - left_closed)):
        # select gate to open
        shot = round((size - 1) * random.random()) + 1
        # do not open winning/selected nor already opened gate, might draw lots for long time if number of gates is big
        while shot == winning or gates[shot - 1] == 1 or shot == selection:
            shot = round((size - 1) * random.random()) + 1
        gates[shot - 1] = 1

    # print('empty:', end=' ')
    # for i in range(size):
    #     if gates[i] == 0:
    #         print(i + 1, sep=' ')
    # print('winning:', winning)
    # print('selection:', selection)
    return selection == winning


def main():
    size = 10
    winners = 0
    num_of_tries = 1000
    for i in range(num_of_tries):
        if draw_lots(size):
            winners += 1
    print(f'Number of gates in game: {size}. After {num_of_tries} games you won only {winners} times.')


if __name__ == '__main__':
    main()
