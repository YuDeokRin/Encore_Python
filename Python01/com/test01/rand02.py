# -*-coding:utf-8 -*-


import random

# 로또 번호를 출력하는 함수
# 1 ~ 45 사이의 숫자 6개를 작은 수 부터 순서대로 정렬해서 출력하자 
def lotto():
    result = set()
    while len(result) <= 6:
        ran = random.randint(1, 45)
        result.add(ran)
    res = sorted(result) # sorted : 리스트 만들어서 sort를 해준다.  
    print(res)
    
    
if __name__ == '__main__':
    lotto()
