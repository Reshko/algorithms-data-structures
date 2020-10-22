from random import randint

arr = [randint(-10, 30) for i in range(10)]
print(arr)

for i in range(0,len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]


print(arr)