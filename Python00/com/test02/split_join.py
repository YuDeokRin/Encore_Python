import re

#split
str01 = 'Hello, world!\nHello, python!'
print(str01)

arr01 = str01.split(' ')
print(arr01)

arr02 = str01.split(' ', 1)
print(arr02)


arr03 = re.split('[\s]|[,]',str01)
print(arr03)


# join

arr04 = ['1','2','3','4']
print(arr04)
print('+'.join(arr04))


a = '+'.join(arr04)
print(eval(a))






