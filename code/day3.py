import sys
from helperfunc import *
import re

def prepare_input(input_file):
    with open(input_file, 'r') as file:
        mult_tuples = multiply_occurences(file.read())
    return mult_tuples

def prepare_input_2(input_file):
    mult_tuples = []
    with open(input_file, 'r') as file:
        split_text = re.split("don't\(\)", file.read())

    mult_tuples += multiply_occurences(split_text[0])
    for split in split_text[1:]:
        do_split = re.split("do\(\)", split)
        for i in range(1, len(do_split)):
            mult_tuples += multiply_occurences(do_split[i])
    return mult_tuples



def multiply_occurences(input_text):
    mult_tuples = []
    all_occurences = re.findall("mul\([0-9]+,[0-9]+\)", input_text)
    for occurence in all_occurences:
        mult_tuples.append([int(nr_string) for nr_string in re.findall("[0-9]+", occurence)])
    return mult_tuples

def sum_mult_tuples(mult_tuples):
    sum_of_mults = 0
    for mult_tuple in mult_tuples:
        sum_of_mults += mult_tuple[0] * mult_tuple[1]
    return sum_of_mults

def part1(input_data):
    return sum_mult_tuples(input_data)


def part2(input_data):
    return sum_mult_tuples(input_data)


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input_2(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
