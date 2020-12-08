# Определить, какое число в массиве встречается чаще всего

from random import randint

SIZE = 100
MAX_ITEM = 100
MIN_ITEM = 1

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
number = array[0]
count = 0

for i in range(len(array)):
    elem = 0
    for j in range(len(array)):
        if array[i] == array[j]:
            elem += 1
    if count < elem:
        count = elem
        number = array[i]

print(f'{number}, {count=}')



#check myself
print('-'*100)
print(max(array, key=array.count))
