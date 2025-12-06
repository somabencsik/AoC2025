"""
Day 6 task 1 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/6
"""


def read_file(filename: str) -> list[list[str]]:
    """
    Reads the file and returns a list of instructions.

    Arguments
    ---------
    filename : str
        Name / path to the input file

    Returns
    -------
    list[list[int | str]]
        A list of instructions. An instruction is a list of numbers and the
        last element of the list is the operator
    """
    result = []
    with open(filename, "r") as f:
        for line_idx, line in enumerate(f.readlines()):
            line = line.strip().split()
            for i, v in enumerate(line):
                if i == len(result):
                    result.append([])
                result[i].append(v)
    return result


def solve_math(math_instructions: list[list[str]]) -> int:
    """
    Returns the sum of results of each mathematical instruction.

    Arguments
    ---------
    math_instructions : list[list[int | str]]
        The mathematical instructions that every element is a number except for
        the last one, that is the operator

    Returns
    -------
    int
        The some of results of mathematical instructions
    """
    result = 0
    for math_instruction in math_instructions:
        result += eval(math_instruction[-1].join(math_instruction[:-1]))
    return result


if __name__ == "__main__":
    input_file = "task_input"
    math_instructions = read_file(input_file)
    result = solve_math(math_instructions)
    print(f"{result = }")
