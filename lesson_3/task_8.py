# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

from random import randint

LINE = 4
COLUMN = 4
MINIMUM = 1
MAXIMUM = 100

# Auto-input
# matrix = [[randint(MINIMUM, MAXIMUM) for _ in range(LINE)] for _ in range(COLUMN)]

# Manual - input
matrix = [[int(input("Enter the number for matrix: ")) for _ in range(LINE)] for _ in range(COLUMN)]

print('-' * 30, 'MATRIX', '-' * 30)

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        print(f'{item:>3}', end='')
    print(f'\t{sum_line}')
