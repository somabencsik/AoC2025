"""
Day 6 task 2 of Advent of Code 2025.
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
    with open(filename, "r") as f:
        lines = f.readlines()

    column_widths = []
    column = 1
    for i, c in enumerate(lines[-1][::-1]):
        if c == "*" or c == "+":
            column_widths.append(column)
            column = 0
        else:
            column += 1
    column_widths = column_widths[::-1]
    
    math_instructions = []
    column_width_iterator = 0
    i = 0
    while column_width_iterator < len(column_widths):
        column_width = column_widths[column_width_iterator]
        if column_width_iterator > 0:
            i += column_widths[column_width_iterator - 1] + 1
        new_numbers = [""] * column_width
        for line in lines[:-1]:
            for j in range(len(line[i:i+column_width])):
                new_numbers[j] += line[i:i+column_width][j]

        math_instructions.append([str(int(n)) for n in new_numbers])
        math_instructions[-1].append( lines[-1][i:i+column_width].strip())
        column_width_iterator += 1

    return math_instructions


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
