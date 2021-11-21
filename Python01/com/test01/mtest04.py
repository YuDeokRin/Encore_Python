# -*-coding:utf-8 -*-


def mysum(x,y):
    return 2 * x + y

if __name__ == '__main__' :
    a = mysum(2, 3)
    print(a)
    
    b = lambda x,y : 2 * x + y
    print(b(2,3))