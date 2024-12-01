import sys
from helperfunc import *


def prepare_input(input_file):
    id_list_a = []
    id_list_b = []
    for line in read_input_lines(input_file):
        id_strings = line.split()
        id_list_a.append(int(id_strings[0]))
        id_list_b.append(int(id_strings[1]))
    return id_list_a, id_list_b


def part1(input_data):
    id_list_a, id_list_b = input_data
    id_list_a.sort()
    id_list_b.sort()
    id_difference_sum = 0
    for i in range(len(id_list_a)):
        id_difference_sum += abs(id_list_a[i] - id_list_b[i])
    return id_difference_sum


def part2(input_data):
    id_list_a, id_list_b = input_data
    similarity_score_total = 0
    similarity_scores_dict = {}
    for id_nr in id_list_a:
        if id_nr in similarity_scores_dict:
            similarity_score_total += similarity_scores_dict.get(id_nr)
        else:
            id_occurences = id_list_b.count(id_nr)
            similarity_score = id_nr*id_occurences
            similarity_scores_dict.update({id_nr: similarity_score})
            similarity_score_total += similarity_score
    return similarity_score_total


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
