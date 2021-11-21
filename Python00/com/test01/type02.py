# 문자
# ' ', " "차이없음


# single *1 
a = 'python\'s\nhello,world!'

print(a)

# sing * 3 
b= '''python's
Hello , World!'''

print(b)


# double * 1 
c = "자율주행을 위한 IoT\tBigdata\tAI\n기술융합  \"개발자\"양성과정"
print(c)

#double * 3

d= """자율주행을 위한 IoT Bigdata AI 
기술융합 "개발자" 양성과정"""

print(d)

#raw String 
e = "C:\venvs\myenv\test"
print(e)


f = r"C:\venvs\myenv\test"
print(f)

#문자열 더하기, 곱하기

str01 = "Hello,"
str02 = "World!"
print(str01 + str02)

print(str01 + str02)
print(str01 * 3 + str02)
