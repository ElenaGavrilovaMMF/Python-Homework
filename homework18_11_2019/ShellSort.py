

def insertSort(mass, start, dist):
    i = start
    while i < len(mass) - 1:
        j = int(min(i + dist, len(mass) - 1))
        while j - dist >= 0:
            if mass[j - dist] > mass[j]:
                tmp = mass[j]
                mass[j] = mass[j - dist]
                mass[j - dist] = tmp
            else:
                break
            j -= dist
        i += dist


def sortShell(mass):
    dist = len(mass) / 2
    while dist >= 1:
        step = 0
        while step < dist:
            insertSort(mass, step, int(dist))
            step += 1
        dist /= 2

