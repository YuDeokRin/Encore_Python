# -*- coding:utf-8 -*-

def func01(x,y):
    return x + y

def func02(x,y):
    return x + y, x-y

if __name__ == '__main__':
    a = func01(1,3)
    print(a)
    print(func02(4,7))
    
    b, c = func02(4,7)
    print(b)
    print(c)