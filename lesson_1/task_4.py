# Пользователь вводит номер буквы в алфавите. Определить, какая это буква


a = int(input('Enter the number of the English letter [1-26]: '))
z = 96

if 1 <= a <= 26:
    a = chr(a + z)
    print(f'{a=}')
else:
    print("Invalid input")
