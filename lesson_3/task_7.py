# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


from random import randint

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = -100

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array}')

first_negative = array[0]

for i in range(len(array)):
    if first_negative > array[i]:
        first_negative = array[i]

idx_negative_elem = array.index(first_negative)
first_minimum = array.pop(idx_negative_elem)

second_negative = array[0]
#DRY principals are violated

for k in range(len(array)):
    if second_negative > array[k]:
        second_negative = array[k]

idx_negative_elem = array.index(second_negative)
second_minimum = array.pop(idx_negative_elem)

print(f'{array}')
print(f'{first_minimum=}, {second_minimum=}')
