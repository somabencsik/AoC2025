"""
Day 7 task 2 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/7
"""


def read_file(filename: str) -> list[list[str]]:
    """
    Reads the file and returns the 2D list of str.

    Arguments
    ---------
    filename : str
        Name / path to the input file

    Returns
    -------
    list[list[str]]
        2D list of the tachyon manifold
    """
    result = []
    with open(filename, "r") as f:
        for line in f.readlines():
            result.append([v for v in line.strip()])
    return result


def draw_in_beams(tachyon_manifold: list[list[str]]) -> None:
    """
    Draws in the beams.

    Arguemnts
    ---------
    tachyon_manifold : list[list[str]]
        2D list of the tachyon manifold
    """
    for row_idx, line in enumerate(tachyon_manifold[1:], 1):
        for col_idx, symbol in enumerate(line):
            if symbol == "." and (
                tachyon_manifold[row_idx - 1][col_idx] == "S" or \
                tachyon_manifold[row_idx - 1][col_idx] == "|"
            ):
                tachyon_manifold[row_idx][col_idx] = "|"
            elif (
                symbol == "^" and tachyon_manifold[row_idx - 1][col_idx] == "|"
            ):
                tachyon_manifold[row_idx][col_idx - 1] = "|"
                tachyon_manifold[row_idx][col_idx + 1] = "|"


def get_num(value: str | int) -> int:
    """
    Returns a number of the given value that is either '.' or an integer.

    Arguments
    ---------
    value : str | int
        Value from the tachyon_manifold either '.' or a beam value

    Returns
    -------
    int
        Value of the beam or if it's '.', than 0
    """
    if isinstance(value, str):
        return 0
    return value


def change_beams_to_timeline_numbers(tachyon_manifold: list[list[str]]):
    """
    Turns the beam(|) into a number that is the possible timeline of that beam.

    Arguemnts
    ---------
    tachyon_manifold : list[list[str]]
        2D list of the tachyon manifold
    """
    tachyon_manifold[0][tachyon_manifold[0].index("S")] = 1
    for row_idx, line in enumerate(tachyon_manifold[1:], 1):
        for col_idx, symbol in enumerate(line):
            if symbol != "|":
                continue
            value = 0
            if (
                    col_idx + 1 < len(line) and
                    tachyon_manifold[row_idx][col_idx + 1] == "^" and
                    tachyon_manifold[row_idx][col_idx - 1] == "^"
            ):
                value += get_num(tachyon_manifold[row_idx - 1][col_idx - 1])
                value += get_num(tachyon_manifold[row_idx - 1][col_idx])
                value += get_num(tachyon_manifold[row_idx - 1][col_idx + 1])
            elif (
                    col_idx + 1 < len(line) and
                    tachyon_manifold[row_idx][col_idx + 1] == "^"
            ):
                value += get_num(tachyon_manifold[row_idx - 1][col_idx])
                value += get_num(tachyon_manifold[row_idx - 1][col_idx + 1])
            elif tachyon_manifold[row_idx][col_idx - 1] == "^":
                value += get_num(tachyon_manifold[row_idx - 1][col_idx])
                value += get_num(tachyon_manifold[row_idx - 1][col_idx - 1])
            else:
                value += get_num(tachyon_manifold[row_idx - 1][col_idx])
            tachyon_manifold[row_idx][col_idx] = value


def get_timelines(tachyon_manifold: list[list[str]]) -> int:
    """
    Returns the number of timelines.

    Arguemnts
    ---------
    tachyon_manifold : list[list[str]]
        2D list of the tachyon manifold

    Returns
    -------
    int
        Number of timelines
    """
    draw_in_beams(tachyon_manifold)
    change_beams_to_timeline_numbers(tachyon_manifold)
    return sum([0 if isinstance(v, str) else v for v in tachyon_manifold[-1]])


if __name__ == "__main__":
    input_file = "task_input"
    tachyon_manifold = read_file(input_file)
    timelines = get_timelines(tachyon_manifold)
    print(timelines)
