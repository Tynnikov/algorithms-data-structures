# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

digit = int(input("Enter your integer: "))


# Option 1
def recurcion(digit):
    if digit < 10:
        return digit
    else:
        return str(digit % 10) + str(recurcion(digit // 10))


print(recurcion(digit))

# Option 2
print(str(digit)[::-1])
