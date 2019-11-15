# V 16
# w = cos(a/3)+t+exp(a\m)
# r=0.7*sqrt(3w+j)+|a^2-1|

# for:
# a=1.4, m=6, t=15*10^5, j={0.5, 9.1, 5}

# while
# i=1(0.1)2

# while+for
# m=8(0.2)9, (x)j={0.6, -0.1, 5}
import math

a = 1.4
m = 6
t = 15 * (10 ^ 5)
w = math.cos(a / 3) + t + math.exp(a / m)

print('FOR')
J = {0.5, 9.1, 5}
print('w=', w)
for j in J:
    r = 0.7 * math.sqrt(3 * w + j) + abs(math.pow(a, 2) - 1)
    print('j=', j, 'r=', r)

print('\nWHILE')
j = 1
print('w=', w)
while j <= 2:
    r = 0.7 * math.sqrt(3 * w + j) + abs(math.pow(a, 2) - 1)
    print('j=', j, 'r=', r)
    j += 0.1
    j = float('{:.1f}'.format(j))

print('\nWHILE+FOR')
J = {0.6, -0.1, 5}
m = 8
while m <= 9:
    w = math.cos(a / 3) + t + math.exp(a / m)
    print('w=', w)
    for j in J:
        r = 0.7 * math.sqrt(3 * w + j) + abs(math.pow(a, 2) - 1)
        print('m=', m, 'j=', j, 'r=', r)
    print()
    m += 0.2
    m = float('{:.1f}'.format(m))
