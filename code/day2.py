import sys
from helperfunc import *


def prepare_input(input_file):
    all_reports = []
    lines = read_input_lines(input_file)
    for line in lines:
        all_reports.append([int(level_string) for level_string in line.split()])
    return all_reports

def check_gradual_direction(level_1, level_2, decreasing):
    diff = level_1-level_2
    if decreasing and 0 < diff < 4:
        return True
    if not decreasing and -4 < diff < 0:
        return True
    return False


def part1(input_data):
    nr_of_safe_reports = 0
    for report in input_data:
        direction = (report[0] - report[1]) > 0
        safe = True
        for i in range(len(report)-1):
            if not check_gradual_direction(report[i], report[i+1], direction):
                safe = False
                break
        if safe:
            nr_of_safe_reports += 1
    return nr_of_safe_reports


def part2(input_data):
    nr_of_safe_reports = 0
    for report in input_data:
        direction = (report[0] - report[1]) > 0
        safe = True
        problem_dempener_used = False
        for i in range(len(report) - 1):
            if not check_gradual_direction(report[i], report[i + 1], direction):
                if problem_dempener_used:
                    safe = False
                    break
                else:
                    problem_dempener_used = True
                    if i == 0 or i == 1:
                        direction = (report[2]-report[3]) > 0
                        if check_gradual_direction(report[1], report[2], direction):
                            continue
                        elif i == 1:
                            if not check_gradual_direction(report[0], report[2], direction):
                                safe = False
                                break
                            continue
                    report[i+1] = report[i]
        if safe:
            nr_of_safe_reports += 1
        print(safe)
    return nr_of_safe_reports


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
