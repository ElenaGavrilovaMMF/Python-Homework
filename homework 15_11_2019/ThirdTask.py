# Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом и записать эти суммы в новый список B.
import random

try:
    n = int(input('n:\n'))
    A = []
    while len(A) < n:
        A.append(random.randint(0, 99))
        print(A)
    B = []
    i = 0
    while i < n - 1:
        B.append(A[i] + A[i + 1])
        i += 2
    if n % 2 != 0:  # если длинна списка нечетная (то есть инкс последнего элемента четный, но следующего у него нет) я добавила просто последний элемент
        B.append(A[n - 1])
    print(B)
except ValueError:
    print('You entered the wrong data type.')
