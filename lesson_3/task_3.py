# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

SIZE = 100
MAX_ITEM = 100
MIN_ITEM = 1

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')

max = array[0]
min = array[0]

for i in range(SIZE):
    if max < array[i]:
        max = array[i]
    elif min > array[i]:
        min = array[i]

print(f'{max=}, {min=}')

idx_max = array.index(max)
idx_min = array.index(min)
array[idx_max], array[idx_min] = array[idx_min], array[idx_max]
print(array)
