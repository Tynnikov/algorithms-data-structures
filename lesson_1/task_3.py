# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.


a = ord(input('Enter the letter between [a-z]: '))
b = ord(input('Enter the letter between [a-z]: '))
z = 96

if 97 <= a and b <= 122:
    a -= z
    b -= z
    print(f"{a=}, {b=}")
    c = a - b
    print(f'c={abs(c)}')
else:
    print("It wasn't be a letter")
