"""
Day 7 task 1 of Advent of Code 2025.
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


def get_beam_splits(tachyon_manifold: list[list[str]]) -> int:
    """
    Returns the number of times the beam splitted from it's original position.

    Arguemnts
    ---------
    tachyon_manifold : list[list[str]]
        2D list of the tachyon manifold

    Returns
    -------
    int
        Number of times the beam splitted from it's original position
    """
    result = 0
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
                result += 1
                tachyon_manifold[row_idx][col_idx - 1] = "|"
                tachyon_manifold[row_idx][col_idx + 1] = "|"
    return result


if __name__ == "__main__":
    input_file = "task_input"
    tachyon_manifold = read_file(input_file)
    n_beam = get_beam_splits(tachyon_manifold)
    print(n_beam)
