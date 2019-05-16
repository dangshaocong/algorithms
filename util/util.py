# -*- coding:utf-8 -*-
def exceptFun(fun):
    def inner(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except Exception as e:
            print('--- Exception occur ---')
            print(str(e))
    return inner


