# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Enter digits n elem: '))
count = 1
total = 0
number = 1

while count <= n:
    number /= -2
    total += number
    count += 1

print(f'{total=}')
