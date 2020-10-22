from random import randint

arr = [randint(-10, 30) for i in range(10)]
print(arr)


def find_small(array):
    min_index = 0
    min_value = 0
    for index,value in enumerate(array):
        if value < min_value:
            min_value = value
            min_index = index
    return min_index



a = find_small(arr)

print(a)
