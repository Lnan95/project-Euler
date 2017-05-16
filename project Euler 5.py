'''
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import numpy

# 11 12 13 14 15 16 17 18 19 20
x = 20
num = numpy.array([11,12,13,14,15,16,17,18,19,20])

while 1:
    x += 1
    if all(x % num==0):
        break
print('the smallest positive number is {}'.format(x))