# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

COLUMNS = 4
LINES = 5
MINIMUM = 1
MAXIMUM = 100

matrix = [[randint(MINIMUM, MAXIMUM) for _ in range(COLUMNS)] for _ in range(LINES)]

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', min_list[0])