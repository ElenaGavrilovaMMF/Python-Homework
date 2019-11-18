import math


def stoogeSort(item):
    left = 0
    right = len(item) - 1
    stoogeSortLeftRight(item, left, right)


def stoogeSortLeftRight(item, left, right):
    if item[left] > item[right]:
        tmp = item[left]
        item[left] = item[right]
        item[right] = tmp
    if left + 1 >= right:
        return
    k = math.floor((right - left + 1) / 3)
    stoogeSortLeftRight(item, left, right - k)
    stoogeSortLeftRight(item, left + k, right)
    stoogeSortLeftRight(item, left, right - k)
