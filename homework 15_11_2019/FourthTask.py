# Заменить каждый третий элемент списка полусуммой двух предыдущих.
import random

try:
    n = int(input('Enter the length of the list n:\n'))
    A = []
    while len(A) < n:
        A.append(random.randint(0, 99))
    print(A)
    i = 2
    if len(A) >= 3:
        while i < n:
            A[i] = (A[i - 1] + A[i - 2]) / 2
            i += 3
        print(A)
    else:
        print('List length less than 3')
except ValueError:
    print('You entered the wrong data type.')
