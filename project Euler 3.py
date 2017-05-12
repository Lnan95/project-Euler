'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

x = 600851475143
for i in range(1,10000):
    if x%i == 0:
        x = x/i
        print("公约数为：{}，新的x为：{}".format(i,x))
