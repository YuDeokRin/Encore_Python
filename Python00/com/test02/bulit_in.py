# int()
print(int(True))
print(int(False))

print('------------------')
print(int('1111',2))
print(int('77',8))
print(int('ff',16))


#str()
a = 10

#TypeError: can only concatenate str (not "int") to str
print('a = ' + a) 
print('a =' + str(a) )

print(type(a))