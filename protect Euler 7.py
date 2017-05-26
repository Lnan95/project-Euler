'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

import numpy as np
prime = [2,3,5,7,11,13]
n = 15
while len(prime) <= 10000:
    n += 2
    # num = np.sqrt(n)
    if all((n%(np.array(prime)[prime<=np.sqrt(n)]))!=0):
        prime.append(n)
print("the 10 001st prime number is {}".format(prime[-1]))

# 104743

