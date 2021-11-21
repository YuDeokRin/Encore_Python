# -*-coding:utf-8 -*-


# 5! = 5 * 4 * 3 * 2 * 1 

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def factorial_recursion(n):
    if n == 1:
        return 1
    return n * factorial_recursion(n-1)


if __name__ == '__main__':
    n = int(input('n : '))
    res = factorial(n)
    print(res)
    
    result = factorial_recursion(n)
    print(result)