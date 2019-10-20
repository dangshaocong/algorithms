# -*- coding:utf-8 -*-
# use timeit get the time
from timeit import Timer


def t1():
    l1 = []
    for i in range(0, 1001):
        l1 = l1 + [i]


def t2():
    l1 = []
    for i in range(0, 1001):
        l1.extend([i])


def t3():
    l1 = []
    for i in range(0, 1001):
        l1.append(i)


def t4():
    l1 = [i for i in range(0, 1001)]


def t5():
    l1 = list(range(0, 1001))


print('test list fun')
r1 = Timer('t1()', 'from __main__ import t1')
print('+ use times', r1.timeit(1000))

r2 = Timer('t2()', 'from __main__ import t2')
print('extends', r2.timeit(1000))

r3 = Timer('t3()', 'from __main__ import t3')
print('append', r3.timeit(1000))

r4 = Timer('t4()', 'from __main__ import t4')
print('range', r4.timeit(1000))

r5 = Timer('t5()', 'from __main__ import t5')
print('list range', r5.timeit(1000))
