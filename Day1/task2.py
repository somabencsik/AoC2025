"""
Day 1 task 2 of Advent of Code 2025.
Find the task description here: https://adventofcode.com/2025/day/1
"""
from typing import Literal


MINIMUM_POSITION = 0
MAXIMUM_POSITION = 99
NUMBER_OF_NUMBERS = len(range(MINIMUM_POSITION, MAXIMUM_POSITION)) + 1


def read_file(filename: str) -> list[tuple[str, int]]:
    """
    Reads the file and returns a list of instructions.

    Arguments
    ---------
    filename : str
        Name / path to the input file

    Returns
    -------
    list[tuple[str, int]]
        A list of instruction. 1 instruction is a tuple, first value is
        the direction the second value is the times to do so.
    """
    result = []
    with open(filename, "r") as f:
        for line in f.readlines():
            result.append( (line[0], int(line[1:])) )
    return result


def rotate(
    current_position: int,
    direction: Literal["L", "R"],
    times: int
) -> int:
    """
    Returns the new value after turning the dial.

    Arguments
    ---------
    current_position : int
        The position where the dial stands currently

    direction : "L" | "R"
        The direction to rotate to, left or right

    times : int
        Times to rotate the dial to the given directon

    Returns
    -------
    int
        New value on the dial
    """
    new_value = 0
    if direction == "L":
        new_value = current_position - times
        if new_value < MINIMUM_POSITION:
            new_value = MAXIMUM_POSITION - abs(new_value) + 1
    elif direction == "R":
        new_value = current_position + times
        if new_value > MAXIMUM_POSITION:
            new_value = new_value - MAXIMUM_POSITION - 1
    else:
         print(f"Wrong direction: {direction}")   
    return new_value


def open_safe(instructions: list[tuple[str, int]]) -> int:
    """
    Returns the times the dial points to 0.

    Arguments
    ---------
    instructions : list[tuple[str, int]]
        List of instructions to open the safe. 1 instruction is a tuple:
        first value is the direction, second value is the times to turn
        the dial

    Returns
    -------
    int
        Number of times the dial points to 0
    """
    through_zero = 0
    current_position = 50
    for instruction in instructions:
        direction = instruction[0]
        times = instruction[1]
        if times > NUMBER_OF_NUMBERS:
            through_zero += times // NUMBER_OF_NUMBERS
            times = times % NUMBER_OF_NUMBERS
        previous_position = current_position
        current_position = rotate(current_position, direction, times)
        if direction == "L" and current_position > previous_position:
            through_zero += 1
        elif direction == "R" and current_position < previous_position:
            through_zero += 1
    return through_zero


if __name__ == "__main__":
    input_file = "task_input"
    instructions = read_file(input_file)
    zero_position = open_safe(instructions)
    print(zero_position)
