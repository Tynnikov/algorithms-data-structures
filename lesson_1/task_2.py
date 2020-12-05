
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки
x1 = int(input("Enter integer: "))
x2 = int(input("Enter integer: "))
y1 = int(input("Enter integer: "))
y2 = int(input("Enter integer: "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(k, b)
