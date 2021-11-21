# -*-coding:utf-8 -*-

#pip install numpy
# =>  수치해석 


# pip install matplotlib
# => 그래프

import numpy as np
import matplotlib.pyplot as plt
import random
def plt01():
    x = np.arange(0, 11)
    y = x 
    
    plt.plot(x,y)
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.legend(['y= x'])
    
    plt.show()
    
def plt02():
    y = [random.randint(0, 10) for _ in range(10)]
    x = range(10)
    
    plt.bar(x,y)
    
    
    plt.xlabel(range(11))
    plt.ylabel(range(11))
    
    plt.show()
    
def plt03():
    date = [random.randint(100, 1000) for _ in range(4)]
    
    plt.pie(date)
    
    category = ['1','2','3','4']
    plt.legend(category)
    
    plt.show()
    
if __name__ == '__main__':
    #plt01()
    #plt02()
    plt03()