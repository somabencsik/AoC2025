"""
Day 2 task 2 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/2
"""


def read_file(filename: str) -> list[list[int]]:
    """
    Reads the file and returns a list of list of numbers.

    Arguments
    ---------
    filename : str
        Name / path to the input file

    Returns
    -------
    list[list[int]]
        A list of list of numbers based on the ranges
    """
    ids = []
    with open(filename, "r") as f:
        data = f.read()
        for id_range in data.split(","):
            left = int(id_range.split("-")[0])
            right = int(id_range.split("-")[1])
            ids.append(list(range(left, right + 1)))
    return ids


def is_sequence(number: str, sub_number: str) -> bool:
    """
    Check if a number is built up from the given sub number.

    Arguments
    ---------
    number : str
        The number to check

    sub_number : str
        The number to check with

    Returns
    -------
    bool
        True, if the number is built only from the sub_number, false otherwise
    """
    if len(number) % len(sub_number) != 0:
        return False
    if number.count(sub_number) != len(number) // len(sub_number):
        return False
    return True


def get_wrong_ids(ids: list[list[int]]) -> list[int]:
    """
    Returns the wrong ids in a list.

    Arguments
    ---------
    ids : list[list[int]]
        List of list of numbers to check for wrong ID

    Returns
    -------
    list[int]
        List of wrong ids
    """
    wrong_ids = []
    for id_list in ids:
        for number in id_list:
            number = str(number)
            middle_index = len(number) // 2
            for i in range(middle_index, 0, -1):
                sub_number = number[:i]
                if is_sequence(number, sub_number):
                    wrong_ids.append(int(number))
    return set(wrong_ids)


if __name__ == "__main__":
    input_file = "task_input"
    ids = read_file(input_file)
    wrong_ids = get_wrong_ids(ids)
    print(sum(wrong_ids))
