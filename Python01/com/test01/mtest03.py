# -*-coding:utf-8 -*-

# 1. for문을 사용하여 구구단 전체를 출력하는 함수 gugu()를 만들자.
def gugu():
    print('구구단')
    for i in range(2, 10):
        print(f'<<{i}단>>')
        for j in range(1,10):
            print('%d * %d = %d' % (i,j,i*j))
            print()

# 2. while문을 사용하여 구구단 중 입력된 출력하는 gugudan(x)를 만들자.
def gugudan(dan):
    print('{]단'.format(dan))
    i = 1 
    while i < 10:
        print('%d * %d = %d' % (dan, i , dan*i))
        i += 1
    print()




if __name__ == '__main__':
    gugu()
    dan = input('단 입력:')
    gugudan(int(dan))

