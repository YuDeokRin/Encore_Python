
# java
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()


#python
for i in range(5):
    print('{:<5}'.format('*'*(i+1)))
    
print()
    
for i in range(6,0,-1):
    print('{:<5}'.format('*'*(i-1)))    
    

for i in range(1,11,2):
    print('{:^10}'.format('*'*i))
    

#강사님 
for i in range(5):
    print('*' *(5-i))
print()

for i in range(5):
    print(' '* (4 - i) + '*'*(i+1))
print()


for i in range(5):
    print(' ' *(i) + '*' * (5*i))
print()


for i in range(5):
    print(' ' * (4 - i) + '*' * (2*i + 1))
    