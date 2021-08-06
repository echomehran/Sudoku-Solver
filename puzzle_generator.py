# Sudoku generator
# Part one >>> create a random sudoku solution board

import random

base = 3
side = base * base


def pattern(r, c):
    """pattern for a baseline valid solution"""
    return (base * (r % base) + r // base + c) % side


def shuffle(s):
    """randomize rows, columns and numbers (of valid base pattern)"""
    return random.sample(s, len(s))


rbase = range(base)
rows = [g * base + r for g in shuffle(rbase) for r in shuffle(rbase)]
cols = [g * base + c for g in shuffle(rbase) for c in shuffle(rbase)]
nums = shuffle(range(1, base * base + 1))

board = [[nums[pattern(r, c)] for c in cols] for r in rows]


# Part two >>> remove some of the numbers to create the puzzle
# Notice that there must be at least 17 numbers in a puzzle

def board_maker():
    """remove some of the numbers based on user response to generate a puzzle with different difficulties"""

    print('\n*** Level of Difficulty ***\n')
    print("1.Beginner")
    print("2.Intermediate")
    print("3.Advanced")
    level = int(input('\nPlease enter the level of difficulty as per your choice: '))

    if level == 1:
        inp = 35
    elif level == 2:
        inp = 20
    else:
        inp = 8

    n = 81
    while n > inp:
        for i in board:
            random_index = random.randint(0, len(i) - 1)
            i[random_index] = 0
            n -= 1


board_maker()
