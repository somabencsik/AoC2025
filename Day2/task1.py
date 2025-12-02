"""
Day 2 task 1 of Advent of Code 2025.
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
            number_length = len(number)
            if number_length % 2 != 0:
                continue
            if number[: number_length // 2] == number[number_length // 2 :]:
                wrong_ids.append(int(number))
    return wrong_ids


if __name__ == "__main__":
    input_file = "task_input"
    ids = read_file(input_file)
    wrong_ids = get_wrong_ids(ids)
    print(sum(wrong_ids))
