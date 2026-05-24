#List Compreshsion Magic
sysmbol = '$%$$$'
beyond_ascii = [ord(s) for s in sysmbol if ord(s) > 127]
print(beyond_ascii)

# Lambda = passing multiple functional arugument in single expressoin 
add = lambda x, y : x + y
print(add(3, 5))

nums_q1 = [3, 2, 4, 1]
sorted_nums = sorted (nums_q1, key=lambda x: x)
print(sorted_nums)

# One Line Code Factorial
facto = lambda n:[1,0][n>1] or facto(n-1)*n
print(facto(7))

funcs = [lambda x: x + i for i in range(3)]
print([f(0) for f in funcs])

############### Map #Map #Map #Map #Map #Map ################################
my_list = range(10)
squaredNumbers = list(map(lambda x: x**2, my_list))
print (squaredNumbers)
nums_q3 = [1, 2, 3, 4, 5]

#list whose elements are square of even number
x = list(map(lambda x: x**2, filter(lambda x: x%2==0, range(10))))
print(x)

nums = [1, 2, 3]
result = list(map(lambda x: x*3, nums))
print(result) # Output: [3, 6, 9]

# Filter ###### Filter ###### Filter  Filter  Filter  Filter
my_list = range(10)
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

iv_f = list(filter(lambda x: x>3, nums_q3))
print(iv_f) # Output: [4, 5]

#The map & filter strugle
beyond_ascii1 = list(filter(lambda c: c > 127, map(ord, sysmbol)))
print(beyond_ascii1)

words = ["deepak", "Python", "java", "javastring", "css", "html"]
# Using filter() to find words starting with "java"
filtered_words = list(filter(lambda word: word.startswith("java"), words))
print(filtered_words)

#One line code prime numbers
prime_num = list(filter(lambda x:all(x%y != 0 for y in range(2, x)), range(2, 20)))
print(prime_num)

#Reduce  Reduce  Reduce  Reduce  Reduce  Reduce
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x,y: x*y, nums)
print(product)




x = lambda a : a +10
print (x(5))

x = lambda a,b : a * b
print (x(6,5))


my_list = [2, 23, 4, 6, 11, 45]

new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

my_list = [1, 5, 4, 7, 8, 11, 3]

new_list= list(map(lambda x: x*2 , my_list))
print(new_list)