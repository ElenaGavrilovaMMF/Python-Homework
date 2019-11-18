"""Процедура добавления объекта в бинарное дерево имеет среднюю алгоритмическую сложность порядка O(log(n)).
Соответственно, для n объектов сложность будет составлять O(n log(n)), что относит сортировку с помощью двоичного дерева к группе
«быстрых сортировок». Однако, сложность добавления объекта в разбалансированное дерево может достигать O(n),
что может привести к общей сложности порядка O(n²).
Наглядгный гиф: http://algolab.valemak.com/tree-binary"""

"""Вообще, бинарное дерево по определению не имеет повторяющихся элементов.
Но дабы не выбрасывать повторяющийся эелемнт из массива (он же нам нужен целиком),
повторяющийся элемент будет идти в правую ветку (как больший элемент) или, другими словами, 
левая ветка - это меньше, а правая - больше или равно"""


class Tree:
    __left = None
    __right = None
    __key = 0
    __sortTreeResult = []

    def __init__(self, key):
        self.__key = key

    def addTree(self, tree):
        if tree.getKey() < self.__key:
            if self.__left is not None:
                self.__left.addTree(tree)
            else:
                self.__left = tree
        else:
            if self.__right is not None:
                self.__right.addTree(tree)
            else:
                self.__right = tree

    def seeTree(self):
        if self.__left is not None:
            self.__left.seeTree()
        self.__sortTreeResult.append(self.__key)
        if self.__right is not None:
            self.__right.seeTree()
        return self.__sortTreeResult

    @staticmethod
    def getSortBinaryTree(mass):
        i = 1
        tree = Tree(mass[0])
        while i < len(mass):
            tree.addTree(Tree(mass[i]))
            i += 1
        mass = tree.seeTree()

    def getKey(self):
        return self.__key
