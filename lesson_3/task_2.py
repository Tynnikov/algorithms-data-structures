# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа

from random import randint

SIZE = 1000
MAX_ITEM = 10000
MIN_ITEM = 10

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
data = list()
for i in range(SIZE):
    if i % 2 == 0:
        data.append(array[i])

print(data)
