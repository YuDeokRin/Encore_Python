#tuple (list와 거의 같다.)

# 생성자 사용
a = tuple()
print(a)
#a.append(1)
#print(a)






b = [1,2,3,4,5]


# () 사용
c = (3,2,1,2)
print(c)


d = b + c 
print(d)

# tuple -> list
e = list(d)
print(e)
print(type(e))


#unpacking 
g = (1,2,3,4)
print(g)

g1,g2,g3,g4 = g 
print(g1)
print(g2)
print(g3)
print(g4)

