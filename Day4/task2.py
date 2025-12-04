"""
Day 4 task 2 of Advent of Code 2025.
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
        2D representation of papers.
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
                tmp_list = list(paper_map[i])
                tmp_list[j] = "x"
                paper_map[i] = "".join(tmp_list)
                result += 1
    return result


def redraw_map(paper_map: list[list[str]]) -> None:
    """
    Redraws the paper map, replaces "x" (previously picked up papers) with ".".

    Arguments
    ---------
    paper_map : list[list[str]]
        2D representation of papers

    Returns
    -------
    None
        The replace happens in-place
    """
    for i in range(len(paper_map)):
        for j in range(len(paper_map[i])):
            if paper_map[i][j] == "x":
                tmp_list = list(paper_map[i])
                tmp_list[j] = "."
                paper_map[i] = "".join(tmp_list)


def get_accessible_papers_with_removal(paper_map: list[list[str]]) -> int:
    """
    Returns the number of paper rolls that can be accessed by forkflift
    iteratively. Once a paper is picked up, forklifts go again until they can't
    pick up anymore.

    Arguments
    ---------
    paper_map : list[list[str]]
        2D representation of papers

    Returns
    -------
    int
        Total number of accessible papers with iterations
    """
    result = 0
    while accessible_papers(paper_map) != 0:
        result += accessible_papers(paper_map)
        redraw_map(paper_map)
    return result


if __name__ == "__main__":
    input_file = "task_input"
    paper_rolls = read_file(input_file)
    papers = get_accessible_papers_with_removal(paper_rolls)
    print(f"{papers = }")
