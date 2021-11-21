# -*-coding:utf-8 -*-


# arg : arguments

def test01(*args):
    for arg in args:
        print(arg)
        
# kwargs : keyward arguments
def test02(**kwargs):
    for k, v in kwargs.items():
        print(k,v,sep='->')     
        
#입력 순서 중요 !
def test03(*args, **kwargs):
    print(args)
    print(kwargs)
        
if __name__ == '__main__':
    test01([1,2,3,4,5])
    test01(*[1,2,3,4,5])
    test02(a=1, b=2, c=3)
    test02(**{'a':4, 'b':5, 'c':6})
    
    test03(*[1,2,3,4,5], **{'a':7, 'b':8, 'c':9})