# -*- coding:utf-8 -*-
# python에서의 인코딩


def func01() :
    print('함수1 입니다.')
    
def func02() :
    return '함수2 입니다'

def func03():
    return {1: 'a', 2: 'b'}

#호출 func01()     


#java에서의 main method
if __name__ == '__main__':
    print('프로그램 시작 시 가장 먼저 호출!')
    func01()
    print(func02())
    print(func03())
    print(func03()[2])