"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import numpy as np
a = 0

while a<333:
    a += 1
    a2 = pow(a,2)
    b = a
    while b < 500:
        b += 1
        b2 = pow(b, 2)
        if np.sqrt(a2 + b2) + a + b == 1000:
            print("abc为{}".format(a*b*np.sqrt(a2 + b2)))
            a  = 333
            break
