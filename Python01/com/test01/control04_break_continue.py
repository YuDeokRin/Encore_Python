# break 

i = 1 
while i <= 10:
    print(i)
    
    if i > 5:
        break
    
    i +=1
else : 
    #출력 X 
    print('i',i)
    
    
#continue

for i in range(1,10):
    if i % 2 ==0:
        continue
    
    print(i)
    
else:
    print('i',i)