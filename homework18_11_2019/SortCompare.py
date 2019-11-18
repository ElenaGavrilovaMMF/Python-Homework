import random
import datetime
import prettytable
import matplotlib.pyplot as plt

from ShellSort import sortShell
from SortBinaryTree import Tree
from StoogeSort import stoogeSort

# Шаблон для вывода информации и генерация списка для тестирования взяла с лекции
# взяла с лекции (добавила третью сортировку в вывод).
table = prettytable.PrettyTable(
    ["Размер списка", "Время бинарного дерева", "Время Stooge sort", "Время сортировки Шелла"])
x = []
y1 = []
y2 = []
y3 = []

# Взяла меньше размер, потому что Stoogesort и Shell медленные. Долго думает.
for N in range(1000, 2001, 500):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    B = A.copy()
    C = A.copy()

    t1 = datetime.datetime.now()
    Tree.getSortBinaryTree(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Сортировка бинарным деревом   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    stoogeSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Stooge sort   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    sortShell(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Сортировка Шелла   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    table.add_row(
        [str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.show()
