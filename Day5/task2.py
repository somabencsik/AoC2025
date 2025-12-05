"""
Day 5 task 2 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/5
"""


def read_file(filename: str) -> tuple[list[int, int], list[int]]:
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
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                break
            left = int(line.split("-")[0])
            right = int(line.split("-")[1])
            fresh_id_ranges.append(range(left, right + 1))
    return fresh_id_ranges


def get_number_of_fresh_ids(fresh_id_ranges: list[range]) -> int:
    """
    Returns the number of fresh ids.

    Arguments
    ---------
    fresh_id_ranges : list[range]
        List of ranges of the fresh ingredients

    available_ids : list[int]
        Ingerdient ids to check if fresh

    Returns
    -------
    int
        Number of fresh ingredient ids
    """
    fresh_id_ranges.sort(key=lambda element: element.start)
    id_sum = 0

    last_range = range(0, 0)
    for fresh_id_range in fresh_id_ranges:
        if fresh_id_range.start in last_range:
            if fresh_id_range.stop not in last_range:
                id_sum += fresh_id_range.stop - last_range.stop
                last_range = range(last_range.start, fresh_id_range.stop)
        else:
            id_sum += len(fresh_id_range)
            last_range = fresh_id_range

    return id_sum


if __name__ == "__main__":
    input_file = "task_input"
    fresh_id_ranges = read_file(input_file)
    number_of_fresh_ids = get_number_of_fresh_ids(fresh_id_ranges)
    print(f"{number_of_fresh_ids = }")
