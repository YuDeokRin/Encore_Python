# dictionary  = java에 map 비슷


#생성자 사용
dict01 = dict()
print(dict01)
dict01['k1'] = 'v1'
dict01[2] = 'two'
print(dict01) 


# {} 사용
dict02 = {'one' : 1, 2: 'two'}
print(dict02)

print(dict01.get('k1'))
print(dict02[2])


#dict01에서 key들만 가지고 오고 싶다
print(dict01.keys())
print(type(dict01.keys()))
print(list(dict01.keys())[1])
#dict02에서 value들만 가지고 오고 싶다
print(dict02.values())
print(type(dict02.values()))