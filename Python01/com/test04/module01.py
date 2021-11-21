# -*-coding:utf-8 -*-

#import math
#math라는 module(library)을 가져와서 사용하겠다.

# math라는 module을 m이라고 부르겠다.
#import math as m

from math import pi

def circle(r):
    #return math.pi * r * r
#    return m.pi * r * r
    return pi * r * r


if __name__ == '__main__':
    r = int(input('반지름 : '))
    print('반지름이 {} 인원의 넓이는 {} 입니다.'.format(r,circle(r)))