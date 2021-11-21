#for

subjects = ['java','database','spring','python']

for sub in subjects :
    print(sub, end=' ')
else :
    print('재밌다!')


#for i in range(1, 101):
#    print(i)
    
    
    
    
# 구구단 출력
# 2 * 1 = 2;
# 2 * 2 = 4;
#......

for i in range(2,10):
    for j in range(1,10):
        print(i,'*',j,'=',(i*j),sep='    ')
        
# 1 ~ 10 까지
for i in range(1, 11):
    print(i, end='\t')
print()

#10 ~ 1 까지
for i in range(10, 0, -1):
    print(i, end='\t')
    

