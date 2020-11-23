# Определить, является ли год, который ввел пользователь, високосным или не високосным

a = int(input('Enter the number: '))

if a % 4 == 0:
    if a % 100 != 0 or a % 400 == 0:
        print('leap year')
    else:
        print('Common year')
else:
    print('Common year')
