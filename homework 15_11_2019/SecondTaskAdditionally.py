"""2. Торговая фирма в первый день работы реализовала товаров на P тыс. руб.,
а затем ежедневно увеличивала выручку на 3%. Какой будет выручка фирмы в
тот день, когда она впервые превысит заданное значение Q? Сколько дней
придется торговать фирме для достижения этого результата?"""
try:
    P = int(input('Enter P:\n'))
    Q = int(input('Enter Q:\n'))
    day = 1
    while P < Q:
        P += P * 0.03
        day += 1
    print('Day №', day, 'P=', P, 'Q=', Q)
except ValueError:
    print('You entered the wrong data type.')
