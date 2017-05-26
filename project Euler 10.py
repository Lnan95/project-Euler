'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import numpy as np
prime = [2,3,5,7]
n = 9
while n <= 2000000:
    n += 2
    if all(n%(np.array(prime)[prime<=np.sqrt(n)])!=0): #  the prime of n must be less than sqrt(n)
        print(n)
        prime.append(n)
print("sum of all the primes below two million. is {}".format(sum(prime))) # 142913828922


