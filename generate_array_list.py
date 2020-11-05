from random import randint


def create_array(lenght=10, max_el=30):
    arr = [randint(0, max_el) for i in range(lenght)]
    return arr
