# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = -100

array = [randint(MIN_ITEM, MAX_ITEM)  for _ in range(SIZE)]
print(f'{array}')

negative_elem = array[0]

for i in range(len(array)):
    if negative_elem > array[i]:
        negative_elem = array[i]

idx_negative_elem = array.index(negative_elem)
print(f'The most negative digit is {negative_elem} and his index is {idx_negative_elem}')



#check myself
print('-'*100)
print(min(array))









#
#
#
# max = array[0]
# min = array[0]
#
# for i in range(SIZE):
#     if max < array[i]:
#         max = array[i]
#     elif min > array[i]:
#         min = array[i]
#
# print(f'{max=}, {min=}')
#
# idx_max = array.index(max)
# idx_min = array.index(min)
# array[idx_max], array[idx_min] = array[idx_min], array[idx_max]
# print(array)