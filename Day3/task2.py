"""
Day 3 task 2 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/3
"""
from copy import deepcopy


JOLTAGE_LENGTH = 12
POSSIBLE_NUMBERS = list(range(1,10))


def read_file(filename: str) -> list[list[int]]:
    """
    Reads the file and returns a list of banks.

    Arguments
    ---------
    filename : str
        Name / path to the input file

    Returns
    -------
    list[list[int]]
        List of banks. 1 bank is a list of int
    """
    banks = []
    with open(filename, "r") as f:
        for line in f.readlines():
            banks.append( [int(v) for v in line.strip()] )
    return banks


def get_next_valid_maximum(
    bank: list[int],
    numbers_left: int
) -> tuple[int, int]:
    """
    Returns the next valid and biggest number's index and value
    in the given bank.

    Arguments
    ---------
    bank : list[int]
        The list of joltages

    numbers_left : int
        Numbers left from the total joltage

    Returns
    -------
    tuple[int, int]
        Index of the biggest valid number and the value
    """
    highest_value_index = 0
    for i in POSSIBLE_NUMBERS[::-1]:
        if i not in bank:
            continue
        if bank.index(i) + numbers_left >= len(bank):
            continue
        highest_value_index = bank.index(i)
        break
    return highest_value_index, bank[highest_value_index]


def get_total_joltage(banks: list[list[int]]) -> int:
    """
    Returns the total output joltage of every bank.

    Arguments
    ---------
    banks : list[list[int]]
        List of banks. 1 bank is a list of integers

    Returns
    -------
    int
        Total ouput joltage
    """
    total_joltage = 0
    for bank in banks:
        bank_to_give = deepcopy(bank)
        result = []
        for i in range(JOLTAGE_LENGTH):
            index, value = get_next_valid_maximum(
                bank_to_give,
                JOLTAGE_LENGTH - 1 - i
            )
            bank_to_give = bank_to_give[index + 1:]
            result.append(value)
        total_joltage += int("".join([str(v) for v in result]))
    return total_joltage


if __name__ == "__main__":
    input_file = "task_input"
    banks = read_file(input_file)
    total_joltage = get_total_joltage(banks)
    print(f"{total_joltage = }")
