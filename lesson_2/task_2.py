# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

digit = input("Enter integer: ")
even = 0
odd = 0

for i in digit:
    i = int(i)
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(f'{even=}, {odd=}')
