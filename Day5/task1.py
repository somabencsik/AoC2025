"""
Day 5 task 1 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/5
"""


def read_file(filename: str) -> tuple[list[range], list[int]]:
    """
    Reads the file and returns a list of fresh ingredient ids and the
    available ingredients.

    Arguments
    ---------
    filename : str
        Name / path to the input file

    Returns
    -------
    tuple[list[range], list[int]]
        The first value of the tuple is the list of fresh ingredient
        ranges the second value of the tuple is the list of ingredients
    """
    fresh_id_ranges = []
    available_ids = []
    add_to_available = False
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                add_to_available = True
                continue
            if add_to_available:
                available_ids.append(int(line))
                continue
            left = int(line.split("-")[0])
            right = int(line.split("-")[1])
            fresh_id_ranges.append(range(left, right + 1))
    return fresh_id_ranges, available_ids


def get_fresh_from_available_ids(
    fresh_id_ranges: list[range],
    available_ids: list[int]
) -> int:
    """
    Returns the int of how many fresh ids are in the available ids list.

    Arguments
    ---------
    fresh_id_ranges : list[range]
        List of ranges of the fresh ingredients

    available_ids : list[int]
        Ingerdient ids to check if fresh

    Returns
    -------
    int
        Number of fresh ingredients from the available ingredients
    """
    fresh_ids = 0
    for a_id in available_ids:
        for id_range in fresh_id_ranges:
            if a_id not in id_range:
                continue
            fresh_ids += 1
            break
    return fresh_ids


if __name__ == "__main__":
    input_file = "task_input"
    fresh_id_ranges, available_ids = read_file(input_file)
    n_fresh_ids = get_fresh_from_available_ids(
        fresh_id_ranges, available_ids
    )
    print(n_fresh_ids)
