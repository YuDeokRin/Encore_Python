
#산술연산

a = 21
b =2
print(a + b)
print(a - b)
print(a * b)
print(a ** b)   # 거듭제곱
print(a / b)   
print(a // b)   # floor division
print(a % b)    # modulo

#비교 연산

a, b = 5,3
print(a == b)
print(a != b)
print(a > b)
print(a <= b)
print(a is b)
print(a is not b)


print('-----------')
print(True or True)
print(False or True)
print(False and True)
print(False and False)


#범위연산
#range(n) : 0 ~ n-1까지
#range(n,m) : 
list01 = list(range(100))
print(list01)
list02 = list(range(50,100))
print(list02)

#slice
#[start:end] :start ~ end-1까지
#[start:end: step] : start, start +step, start + step+ step, ..., end -1 까지

print(list01[2])
print(list01[12:49])
print(list01[12: 49: 3]) # 12부터 +3 씩 해서 48까지 


#문자열 slice
str01 = 'hello world!'
print(str01)
print(str01[4])

#hello만 출력
print(str01[0:5])
print(str01[:5])
print(str01[6:])


#거꾸로 출력하자.
print(str01[: : -1])

#Hello world!
print(str01[-1])
print(str01[-6: ])


print(str01[0 : 4]* 3)




#멤버연산
list02 = [0,1,2,3,4,5]
print(3 in list02)
print(5 in list02)
print(7 not in list02)











