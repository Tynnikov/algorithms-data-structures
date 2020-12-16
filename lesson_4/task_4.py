# Написать два алгоритма нахождения i-го по счёту простого числа
# Первый — с помощью алгоритма «Решето Эратосфена»


def sieve(n):
    digit = n
    n *= 3
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    print(b)
    print(b[digit - 1], 'sieve')

sieve(2)
# # 3
sieve(5)
# # 11

# Второй — без использования «Решета Эратосфена».

def prime(n):
    numbers = list(range(1, n+1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    lst = list(filter(lambda x: x != 0, numbers))
    if n == 1:
        print(2)
    else:
        digit = lst.index(n)
        print(lst[digit])

prime(5)
# 7
prime(1)
# 2




