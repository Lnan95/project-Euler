'''
1.If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''

def f(number):
    s  = 0
    for i in range(number):
        if (i // 3) * 3 == i or (i // 5) * 5 == i:
            s += i
    return s

def f2(number):
    s = 0
    for j in range(number):
        if j % 3 == 0 or j % 5 == 0:
            s += j
    return s

import cProfile
def test(fun,arg,time=10000):
    for i in range(time):
        fun(arg)


cProfile.run('test(f,1000)') # total time : 1.619
cProfile.run('test(f2,1000)') # total time : 1.062



# %求余的方法值得学习