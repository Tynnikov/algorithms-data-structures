# Diagram link: https://drive.google.com/file/d/1q9BKvVrIQycmMT7Ft9oEay4Z3nCttNMK/view?usp=sharing


# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
n = int(input("Enter three-digit number: "))

a = n % 10
b = int(n / 10) % 10
c = n // 100

m = a + b + c
s = a * b * c

print(m, s)
