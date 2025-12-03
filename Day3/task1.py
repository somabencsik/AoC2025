"""
Day 3 task 1 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/3
"""


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


def get_maximum_pair(bank: list[int]) -> int:
    """
    Get the biggest number pair from the bank.

    Arguments
    ---------
    bank : list[int]
        A bank: list of integers

    Returns
    -------
    int
        The highest possible pair combined in the bank
    """
    current_biggest_pair = 11
    for i, left in enumerate(bank[:-1]):
        for right in bank[i + 1:]:
            test_number = left * 10 + right
            current_biggest_pair = max(test_number, current_biggest_pair)
    return current_biggest_pair


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
    maximum_joltage = []
    for bank in banks:
        maximum_joltage.append(get_maximum_pair(bank))
    return sum(maximum_joltage)


if __name__ == "__main__":
    input_file = "task_input"
    banks = read_file(input_file)
    total_output = get_total_joltage(banks)
    print(total_output)
