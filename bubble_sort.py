from generate_array_list import create_array


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
    return array


def benchmark(n=[100, 1000, 10_000, 100_000]):
    from time import time
    b0 = []  # bubble sort
    b1 = []
    for i in n:
        arr = create_array(i, i)

        t0 = time()
        sort_arr = bubble_sort(arr)
        t1 = time()
        b0.append(t1 - t0)

        t0 = time()
        sort_arr = sorted(arr)
        t1 = time()
        b1.append(t1 - t0)

    for index,value in enumerate(n):
        print(f'Value){value} | {b0[index]} | {b1[index]}')



if __name__ == '__main__':
    benchmark()
