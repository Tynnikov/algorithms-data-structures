# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя
link = None


def check_digits():
    digit1 = int(input("Enter the number one: "))
    digit2 = int(input("Enter the number two: "))
    return digit1, digit2


def calculate(digit1, symbol, digit2):
    if symbol == "+":
        print(digit1 + digit2)
    elif symbol == "-":
        print(digit1 - digit2)
    elif symbol == "*":
        print(digit1 * digit2)
    elif symbol == "/":
        if digit2 == 0:
            print("You can't to divide by zero")
            digit2 = int(input("Enter the number two: "))
            print((digit1 / digit2))
        else:
            print(digit1 / digit2)
    else:
        print('You need to use "+", "-", "*", "/"')


def calc():
    while True:
        digit1, digit2 = check_digits()
        symbol = input("Enter the symbol: ")
        if symbol == "0":
            break
        calculate(digit1, symbol, digit2)


calc()
