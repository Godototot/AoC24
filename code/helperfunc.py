from operator import methodcaller


def read_input_lines(file_name):
    """takes file and returns strings for each line, removing the 'new line'"""
    lines = open(file_name, 'r').readlines()
    return list(map(methodcaller('replace', '\n', ''), lines))


def add_tuple(a, b):
    """Adds each element of two tuples of same length."""
    if len(a) != len(b):
        raise Exception("Tuples are of different lengths")
    return tuple(a[i]+b[i] for i in range(len(a)))


def alt_module(i, length):
    """Alternative version of modulo that stops does not wrap negative values up into positive."""
    if i < 0:
        return (i % length)-length
    else:
        return i % length

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Coordinates):
            return Coordinates(self.x+other.x, self.y+other.y)
        else:
            raise TypeError("Operation not possible")

    def __str__(self):
        return "["+str(self.x)+"|"+str(self.y)+"]"
