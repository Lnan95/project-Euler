'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
'''
def reverse(word):
    temp = word
    box = [i for i in range(len(word))]
    box.reverse()
    for i in range(len(word)):
        temp[i] = word[box[i]]
    return temp
'''

t = [i for i in range(100,1000)]
t.reverse()
box = []

for i in t:
    for j in t:
        temp = str(i*j)
        if len(temp) %2 == 0:
            if temp[:len(temp)//2] == temp[(len(temp)//2):][::-1]:
                box.append(int(temp))
        else:
            if temp[:len(temp)//2] == temp[(len(temp)//2+1):][::-1]:
                box.append(int(temp))


print('The max number is {}'.format(max(box)))
