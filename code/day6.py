import sys

from helperfunc import *


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    start_pos = Coordinates(0,0)
    lab_map = []
    for i, line_str in enumerate(lines):
        line_str = "B"+line_str+"B"
        lab_map.append(list(line_str))
        start_x = line_str.find("^")
        if start_x!=-1:
            start_pos = Coordinates(start_x, i+1)
    lab_map.insert(0, list('B'*(len(lines[0])+2)))
    lab_map.append(list('B' * (len(lines[0])+2)))
    return start_pos, lab_map

class Directions:
    def __init__(self, dir_string="UP"):
        self.dir_string = dir_string
        if dir_string == "UP":
            self.dir_coords = Coordinates(0,-1)
        elif dir_string == "RIGHT":
            self.dir_coords = Coordinates(1,0)
        elif dir_string == "DOWN":
            self.dir_coords = Coordinates(0,1)
        elif dir_string == "LEFT":
            self.dir_coords = Coordinates(-1,0)
        else:
            raise Exception

    def turn(self):
        if self.dir_string == "UP":
            self.dir_string = "RIGHT"
            self.dir_coords = Coordinates(1,0)
        elif self.dir_string == "RIGHT":
            self.dir_string = "DOWN"
            self.dir_coords = Coordinates(0,1)
        elif self.dir_string == "DOWN":
            self.dir_string = "LEFT"
            self.dir_coords = Coordinates(-1, 0)
        elif self.dir_string == "LEFT":
            self.dir_string = "UP"
            self.dir_coords = Coordinates(0,-1)

    def __eq__(self, other):
        if isinstance(other, Directions):
            return self.dir_string == other.dir_string
        return False

    def __str__(self):
        return self.dir_string

    def __repr__(self):
        return self.dir_string

    def __copy__(self):
        return Directions(self.dir_string)



def part1(input_data):
    current_pos, lab_map = input_data
    moving_dir = Directions("UP")
    next_pos = current_pos + moving_dir.dir_coords
    next_pos_char = lab_map[next_pos.y][next_pos.x]
    lab_map[current_pos.y][current_pos.x] = 'X'
    while next_pos_char!='B':
        if next_pos_char == '.' or next_pos_char == 'X':
            lab_map[current_pos.y][current_pos.x] = 'X'
            current_pos = next_pos
        elif next_pos_char == '#':
            moving_dir.turn()
        next_pos = current_pos + moving_dir.dir_coords
        next_pos_char = lab_map[next_pos.y][next_pos.x]
    lab_map[current_pos.y][current_pos.x] = 'X'

    sum_visited_places = 0
    for line in lab_map:
        sum_visited_places += line.count('X')
    return sum_visited_places

def evaluate_lab_map(current_pos, lab_map):
    dir_map = [[Directions("UP") for i in range(len(lab_map[0]))] for i in range(len(lab_map))]
    moving_dir = Directions("UP")
    next_pos = current_pos + moving_dir.dir_coords
    next_pos_char = lab_map[next_pos.y][next_pos.x]
    lab_map[current_pos.y][current_pos.x] = 'X'
    dir_map[current_pos.y][current_pos.x] = Directions(moving_dir.dir_string)
    while next_pos_char != 'B':
        if next_pos_char == '.':
            lab_map[current_pos.y][current_pos.x] = 'X'
            dir_map[current_pos.y][current_pos.x] = Directions(moving_dir.dir_string)
            current_pos = next_pos
        elif next_pos_char == 'X':
            if dir_map[next_pos.y][next_pos.x] == moving_dir:
                return True
            dir_map[current_pos.y][current_pos.x] = Directions(moving_dir.dir_string)
            current_pos = next_pos
        elif next_pos_char == '#':
            moving_dir.turn()
        next_pos = current_pos + moving_dir.dir_coords
        next_pos_char = lab_map[next_pos.y][next_pos.x]
    lab_map[current_pos.y][current_pos.x] = 'X'
    return False

def part2(input_data):
    current_pos, lab_map = input_data
    sum_of_possible_positions = 0
    for y in range(len(lab_map)):
        for x in range(len(lab_map[0])):
            if lab_map[y][x] == '.':
                new_lab_map = []
                for i, line in enumerate(lab_map):
                    if i == y:
                        new_line = line.copy()
                        new_line[x] = '#'
                        new_lab_map.append(new_line)
                    else:
                        new_lab_map.append(line.copy())
                sum_of_possible_positions += int(evaluate_lab_map(current_pos, new_lab_map))
                print("Checked", x, y)

    return sum_of_possible_positions


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
