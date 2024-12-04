import sys
from helperfunc import *


def prepare_input(input_file):
    return read_input_lines(input_file)

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y



def check_all_directions_XMAS(word_grid, position):
    nr_of_XMAS = 0

    if position.x > 2:
        nr_of_XMAS += int(check_left(word_grid, position))
        if position.y > 2:
            nr_of_XMAS += int(check_up_left(word_grid, position))
        if position.y < len(word_grid)-3:
            nr_of_XMAS += int(check_down_left(word_grid, position))
    if position.x < len(word_grid[0])-3:
        nr_of_XMAS += int(check_right(word_grid, position))
        if position.y > 2:
            nr_of_XMAS += int(check_up_right(word_grid, position))
        if position.y < len(word_grid)-3:
            nr_of_XMAS += int(check_down_right(word_grid, position))
    if position.y > 2:
        nr_of_XMAS += int(check_up(word_grid, position))
    if position.y < len(word_grid)-3:
        nr_of_XMAS += int(check_down(word_grid, position))
    return nr_of_XMAS

def check_right(word_grid, pos):
    if word_grid[pos.y][pos.x+1] != "M":
        return False
    if word_grid[pos.y][pos.x+2] != "A":
        return False
    if word_grid[pos.y][pos.x+3] != "S":
        return False
    return True

def check_left(word_grid, pos):
    if word_grid[pos.y][pos.x - 1] != "M":
        return False
    if word_grid[pos.y][pos.x - 2] != "A":
        return False
    if word_grid[pos.y][pos.x - 3] != "S":
        return False
    return True

def check_up(word_grid, pos):
    if word_grid[pos.y-1][pos.x] != "M":
        return False
    if word_grid[pos.y-2][pos.x] != "A":
        return False
    if word_grid[pos.y-3][pos.x] != "S":
        return False
    return True

def check_down(word_grid, pos):
    if word_grid[pos.y + 1][pos.x] != "M":
        return False
    if word_grid[pos.y + 2][pos.x] != "A":
        return False
    if word_grid[pos.y + 3][pos.x] != "S":
        return False
    return True

def check_up_right(word_grid, pos):
    if pos.x == 1 and pos.y == 9:
        print()
    if word_grid[pos.y-1][pos.x+1] != "M":
        return False
    if word_grid[pos.y-2][pos.x+2] != "A":
        return False
    if word_grid[pos.y-3][pos.x+3] != "S":
        return False
    return True

def check_up_left(word_grid, pos):
    if word_grid[pos.y - 1][pos.x-1] != "M":
        return False
    if word_grid[pos.y - 2][pos.x-2] != "A":
        return False
    if word_grid[pos.y - 3][pos.x-3] != "S":
        return False
    return True

def check_down_right(word_grid, pos):
    if word_grid[pos.y + 1][pos.x+1] != "M":
        return False
    if word_grid[pos.y + 2][pos.x+2] != "A":
        return False
    if word_grid[pos.y + 3][pos.x+3] != "S":
        return False
    return True

def check_down_left(word_grid, pos):
    if word_grid[pos.y + 1][pos.x-1] != "M":
        return False
    if word_grid[pos.y + 2][pos.x-2] != "A":
        return False
    if word_grid[pos.y + 3][pos.x-3] != "S":
        return False
    return True

def check_X_MAS(word_grid, pos):
    #check if borders
    if 0 < pos.x < len(word_grid[0])-1 and 0 < pos.y < len(word_grid)-1:
        #check diagonals
        if ((word_grid[pos.y-1][pos.x-1]=="M" and word_grid[pos.y+1][pos.x+1]=="S") or (
                word_grid[pos.y-1][pos.x-1]=="S" and word_grid[pos.y+1][pos.x+1]=="M")) and (
                (word_grid[pos.y-1][pos.x+1] == "M" and word_grid[pos.y+1][pos.x-1] == "S") or (
                word_grid[pos.y-1][pos.x+1] == "S" and word_grid[pos.y+1][pos.x-1] == "M")):
            return True
    return False


def part1(input_data):
    nr_of_occurences = 0
    for i, line in enumerate(input_data):
        next_occurence = line.find("X")
        while next_occurence > -1:
            nr_of_occurences += check_all_directions_XMAS(input_data, Coordinates(next_occurence, i))
            if next_occurence == len(line):
                break
            next_occurence = line.find("X", next_occurence+1)
    return nr_of_occurences

def part2(input_data):
    nr_of_occurences = 0
    for i, line in enumerate(input_data):
        next_occurence = line.find("A")
        while next_occurence > -1:
            nr_of_occurences += int(check_X_MAS(input_data, Coordinates(next_occurence, i)))
            if next_occurence == len(line):
                break
            next_occurence = line.find("A", next_occurence + 1)
    return nr_of_occurences


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
