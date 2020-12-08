# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

from random import randint

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = -100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')

minimum = array[0]
maximum = array[0]

for i in range(len(array)):
    if minimum > array[i]:
        minimum = array[i]
    elif maximum < array[i]:
        maximum = array[i]

print(f'{minimum=}, {maximum=}')

idx_minimum = array.index(minimum)
idx_maximum = array.index(maximum)
idx_step = idx_maximum - idx_minimum
sum_ = 0

if idx_minimum < idx_maximum:
    for c in range(len(array)):
        if idx_minimum < c < idx_maximum:
            sum_ += array[c]
elif idx_maximum < idx_minimum:
    for c in range(len(array)):
        if idx_maximum < c < idx_minimum:
            sum_ += array[c]

print(f'Summury between minimum and maximum number - {sum_}')

# check myself
print('-' * 100)
print(min(array), max(array))
