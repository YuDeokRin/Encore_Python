#list 

a = list()
print(type(a))


a.append(1)
print(a)
a.append('2')
print(a)
print(a[1])


#a의 1번 인덱스에 있는 갑을 3으로 변경
a[1] = 3

# a 전체 출력
print(a)

a.append(2)
print(a)


# [] 사용
b = [1,2,3,4,5]
print(b)
print(type(b))

#b[5] = 6 
#print(b)

b.reverse()
print(b)

b.sort()
print(b)


c = ['a', 'b','c','d',['e','f','g'], 'h']
print(c)
print(c[3])

print(c[4][2])

d = a  + c 
print(d)


e = b + a 
print(e)