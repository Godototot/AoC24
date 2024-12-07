import sys
from helperfunc import *


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    all_equations = []
    for line in lines:
        result, operants_str = line.split(":")
        operants = operants_str.split()
        all_equations.append((int(result), [int(op) for op in operants]))
    return all_equations

def rec_evaluation(end_result, current_result, operants):
    if len(operants) == 0:
        return current_result == end_result
    else:
        if current_result > end_result:
            return False
        next_operator = operants[0]
        return (rec_evaluation(end_result, current_result+next_operator, operants[1:]) or
                rec_evaluation(end_result, current_result*next_operator, operants[1:]))

def rec_evaluation_2(end_result, current_result, operants):
    if len(operants) == 0:
        return current_result == end_result
    else:
        if current_result > end_result:
            return False
        next_operator = operants[0]
        return (rec_evaluation_2(end_result, current_result+next_operator, operants[1:]) or
                rec_evaluation_2(end_result, current_result*next_operator, operants[1:]) or
                rec_evaluation_2(end_result, int(str(current_result)+str(next_operator)), operants[1:]))



def part1(input_data):
    result_sum = 0
    for equation in input_data:
        if rec_evaluation(equation[0], equation[1][0], equation[1][1:]):
            result_sum += equation[0]
    return result_sum


def part2(input_data):
    result_sum = 0
    for equation in input_data:
        if rec_evaluation_2(equation[0], equation[1][0], equation[1][1:]):
            result_sum += equation[0]
    return result_sum


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
