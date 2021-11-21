# set(집합)
#순서 없고 중복 불가 

#생성자 사용
a = set(['1','2','3','4','4'])
print(a)
print(type(a))


# 생성자에 iterable한 객체를 넣으면, 각각의 요소가 set의 값으로 변환
b = set('hello')
print(b)



# {} 사용 
c = { 'a', 'b','c', 'hello','d'}
print(c)

d = {'a','d','e','f'}
print(d)
d.add('g')
print(d)


#집합 
#합집합
print(c | d)
print(c.union(d))

#교집합
print(c & d)
print(c.intersection(d))
