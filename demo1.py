# -*- coding:utf-8 -*-
import time

start_time = time.time()
# step1
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print("a,b,c:%d.%d, %d" % (a, b, c))    # 227
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000-a-b
#         if a**2 + b**2 == c**2:
#             print("a,b,c:%d.%d, %d" % (a, b, c))   # 1
end_time = time.time()
print('times:%d' % (end_time-start_time))
print('finished')


# 1. times used  2.steps


