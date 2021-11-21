# 피보나치 수열
# 0 1 1 2 3 5 8 13 ... 

#n = input('n : ')
#print(n)
#print(type(n))

#입력한 갯수만큼의 피보나치 수열을 출력하자.
# ex n : 5
# 0 1 1 2 3


n = input('n : ')

a, b = 0, 1
i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a+b
    i += 1
    
    