
from unicodedata import digit


x = 5
print([x for x in range(3)], end=',')
print(x)


def v(p):
    return p
def v2(p):
    return p*2
def v3(p):
    return p*+5 
res = v(v2(v3(1)))
print(res)

def add(x, y =2):
    return x + y
print(add(3))

def test():
    testx = 5
    return testx
#print(testx) # x is local to the function outside it, x is undefined

def func(a, b):
    print(a +b) #none the function print the result but doesnt return anything so it returns none by deafult

def greet(name):
    return f"Why, {name}?"
print(greet("Python")) #O/P Why, Python?

#Postional & Keyword arguments
def info(name, age):
    print(f"{name} of is {age} years old")
info("Bob", 56)
info(age=45, name= "dod")
#Sum of digits or natural number
def sum_of_digit(dig):
    total = 0
    for num in str(dig):
        total += int(num)
    return total
dig = 123
print(sum_of_digit(dig)) #O/P 6

lst =[0,1,2,3]
for lst[-2]in lst:
    print(lst[-2], end=' ') #O/P 0113 #Loop runs: lst[-2] = 0 → list becomes [0, 1, 0, 3] → prints 0 , lst[-2] = 1 → list becomes [0, 1, 1, 3] → prints 1 , lst[-2] = 1 → list remains [0, 1, 1, 3] → prints 1 lst[-2] = 3 → list becomes [0, 1, 3, 3] → prints 3
#--------------------------------------------------------------------------------------------
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)#O/P a is 3 and b is 5 and c is 10
    print(a+b+c) #O/P 28
func(3, c=20) #O/P a is 3 and b is 5 and c is 20

#----------------------------------------------------------------------
fst = ['p', 'y']
sec= fst #fst and sec are pointing to the same memory object  
''' 
fst─┐
    ├──> ['p', 'y']
sec─┘
'''
sec.append(3.2) #Since both point to same list → both change.
print(fst) #O/P ['p', 'y', 3.2]
print(sec) #O/P ['p', 'y', 3.2]
