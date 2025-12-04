"""
Day 4 task 1 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/4
"""


def read_file(filename: str) -> list[list[str]]:
    """
    Reads the file and returns a 2D list of papers.

    Arguments
    ---------
    filename : str
        Name / path to the input file

    Returns
    -------
    list[list[str]]
        2D representation of papers
    """
    result = []
    with open(filename, "r") as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def accessible_papers(paper_map: list[list[str]]) -> int:
    """
    Returns the number of paper rolls that can be accessed by forkflift.

    Arguments
    ---------
    paper_map : list[list[str]]
        2D representation of papers

    Returns
    -------
    int
        Number of accessible paper
    """
    directions = [
        [-1, -1], [-1, 0],
        [-1, 1], [0, 1],
        [1, 1], [1, 0],
        [1, -1], [0, -1]
    ]
    result = 0
    for i in range(len(paper_map)):
        for j in range(len(paper_map[i])):
            if paper_map[i][j] == ".":
                continue
            adjacent_papers = 0
            for direction in directions:
                i_add = direction[0]
                j_add = direction[1]

                if i + i_add < 0:
                    continue
                if i + i_add >= len(paper_map):
                    continue
                if j + j_add < 0:
                    continue
                if j + j_add >= len(paper_map[0]):
                    continue
                
                if paper_map[i + i_add][j + j_add] == "@" or\
                   paper_map[i + i_add][j + j_add] == "x":
                    adjacent_papers += 1
            if adjacent_papers < 4:
                result += 1
    return result


if __name__ == "__main__":
    input_file = "task_example_input"
    paper_rolls = read_file(input_file)
    papers = accessible_papers(paper_rolls)
    print(f"{papers = }")
