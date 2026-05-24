
'''In Python, immutable objects cannot be changed after they are created. Here are examples of each immutable type:'''
name = "Deepak"
age = 24
salary = 123.45
isAdmin = True

print(name, type(name))
print(age, type(age))
print(salary, type(salary))
print(isAdmin, type(isAdmin))
print(name, end='-')
print(age)
num =4, 5, 6
# if we willtake input() the type will print list
print(num, type(num))  #Output: (4, 5, 6) <class 'tuple'>
sas = "1","4","5"
print("darr", type(sas)) #Output: darr <class 'tuple'>
a,b,c = map(int, input().split(","))
print(a) # Output: 4
print(b) # Output: 5
print(c) # Output: 6

# Integer (int) 
a = 10
b = a  # Both 'a' and 'b' point to the same integer object
a = 20  # Reassigning 'a' creates a new integer object
print(a)  # Output: 20
print(b)  # Output: 10
a = 10.10
b = 10.10
print(id(a)) #id will same 
print(id(b)) # id same 
#Why the diffrent variable storing equal values have same memory allocation 
a = 10
b = 8+2
c = 12-2
d = 5*2

print(id(a) == id(b) == id(c) == id(d)) #`True because of small integer caching in python`
print(a == b == c == d) #True because all the variable have same value but they are different object in memory
print(a is b is c is d) # True because of small integer caching in python
print(id(a), id(b), id(c), id(d))

x = [5]
y = x
x[0] += 6
print(x, y, "x=y") #x=y is interpreted as a keyword argument, but print() does not accept x as a valid keyword argument.
# % = modulus (remainder) It gives you what’s left after division.
aa = 10 % 3 #because 10 ÷ 3 = 3 remainder 1
print(aa)
# / = division   It gives you the result of dividing one number by another
ab = 10 / 3 ##because 10 ÷ 3 = 3.3
print(ab)
#// -  floor devision Divides and rounds down to the nearest integer
ac = 10 // 3
print(ac)

# Float (float)#------------------------------------------------------------------
x = 3.14
y = x
x = 2.71  # New float object is created
print(x)  # Output: 2.71
print(y)  # Output: 3.14

#Bool #----------------------------------------------------------------------------
print(bool([]), bool({}), bool({}), bool(""), bool(0), bool(0.0))
print(bool([5]), bool({5:"Dee"}), bool({5}), bool("Deepak"), bool(1), bool(0.5))

#How to Convert decimal to binary?
num = 25
print(format(num, '08b'))  # → 00011001
print(f"{num:b}")     # → '11001'
print(f"{num:08b}")   # → '00011001'
# String (str)
#1. String Basics
s = "Python"
print(type(s))   # <class 'str'>
print(len(s))    # 6

#2. String Assignment & Memory
name = "Alice"
new_name = name
name += " Johnson"  # A new string object is created
print(name)  # Output: Alice Johnson
print(new_name)  # Output: Alice

str1 = "Apple  and Banana"
#str1[6] = "Grapes"
print(str1) #TypeError: 'str' object does not support item assignment
#Accessing Characters
str2  = "Python"
print (str2[1]) #Output y
print (str2[0]) #Output P
print (str2[-1]) #Output n
print (str2[-2]) #Output o

#Slicing Strings
s = "Python Programming"
print(s[0:6])  # Output: Python (from index 0 to 5)
print(s[7:])   # Output: Programming (from index 7 to the end)
print(s[:6])   # Output: Python (from start to index 5)
print(s[-11:]) # Output: Programming (last 11 characters)
print(s[0:12:2]) # Output: Pto rg
print(s[-1::-1]) # Output: 
print(s[::-2])   # gaimrPnhy
print(s[-1::-1]) # gnimmargorP nohtyP
print(s[::-1])   # gnimmargorP nohtyP
 

#String Concatenation And Repetition
first_name = "Alice"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Johnson

#String Repetition  
s = "Hello"
print(s * 3)  # Output: Hello Hello Hello

#String Length
s = "Python"
print(len(s))  # Output: 6

#String Methods
s = "hello"
print(s.capitalize())   # Output: Hello
print(s.upper())        # Output: HELLO
print(s.lower())        # Output: hello
print(s.title())        # Output: Hello
print(s.isdigit())      # Output: False
print(s.isalpha())      # Output: True
print(s.islower())      # Output: True
print(s.isupper())      # Output: False
print(s.isspace())      # Output: False
print(s.rjust(10))      # Output:      hello
print(s.center(10))     # Output:   hello
print(s.find('e'))      # Output: 1
print(s.find('ll'))     # Output: 2
print(s.find('L'))      # Output: -1
print(s.startswith('h'))  # Output: True
print(s.endswith('o'))  # Output: True
#rfind() is a string method in Python used to find the last occurrence of a substring
text = "abc abc abc"
text.find("abc")   # 0
text.rfind("abc")  # 8

s = " Hello Python  "
print(s.strip())   # Output: Python (removes leading and trailing spaces)
print(s.lstrip())  # Output: Python  (removes leading spaces)
print(s.rstrip()) # Output:   Python (removes trailing spaces)
#split multiple lines
data = "  apple \n banana \n mango  "
items = [line.strip() for line in data.split("\n")]
print(items)
#Extract number from structured string
s = "Age:  54 "
age = s.split(":")[1].strip()
print(age)
#Get last word from a sentence
s = "Python is powerful   "
last_word = s.strip().split(" ")[-1]
print(last_word) #Output powerful
#Extract domain from email
email = "user@gmail.com"
domain = email.split("@")[1]
print(domain)

deloitte = "interview@2026"
print(deloitte.split("@")[0]) #Output Interview

#replace() method
s = "Hello World"
print(s.replace("World", "Python"))  # Output: Hello Python
#s.replaceString('cat', 'dog')
#split() method >>> Divides the string into substrings wherever a specified separator occurs and returns these substrings as a lis
s = "Python,Java,C++"
print(s.split(","))  # Output: ['Python', 'Java', 'C++']

#join() method
s = ["Python", "Java", "C++"]
print(", ".join(s))  # Output: Python, Java, C++

deloitte = "interview@2026"
print("".join([char for char in deloitte if char.isalpha()])) #Output I

s = "Python Programming"
print(s.count("m"))  # Output: 2 (count of 'm')

#formating string  
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

#Escape Sequences
print("Hello\nWorld")  # Newline
print("Hello\tWorld")  # Tab
print("Hello\\World")  # Backslash
print('He said, "Hello!"')  # Quotes within quotes
print("He said, 'Hello!'")  # Quotes within quotes  
print("C:\\Users\\Alice")  # Output: C:\Users\Alice

#Raw Strings
print(r"C:\Users\Alice")  # Output: C:\Users\Alice

#string immutability
s = "Python"
#s[0] = "h"  # Raises a TypeError
s = "J" + s[1:]  # Correct way to modify
s1 = s[:0] +"j" + s[1:] #jython
s2= s[0:3] + "D" + s[4:] #JytDon
print(s)  # Output: Jython
print(s1)  #output: Jython
print(s2) #Output : JytDon
x_s = "python" 
y_s=15
print("Welcome to " + x_s +" programming where the value of y is " + str(y_s))
s23 = "abcdefh"
new_s23 = s23.partition("cd")
print (new_s23)
#sting membership
s = "Python Programming"
print("P" in s)  # Output: True
print("p" in s)  # Output: False
print("j" not in s)  # Output: True
print("Python" in s)   # True
print("Java" in s)     # False

s21 = "Hello"
s22 = "Hello"
s23 = "Hell"
s24 = s23 + "o"
print(s21 == s22)  # Output: True (same content)
print(s21 == s24)  # Output: True (same content)
print(s21 is s22)  # Output: True (same object in memory)
print(s21 is s24)  # Output: False (different object in memory)
#is : is the memory location same?
#== : is the value same?
#python allocates same location to variables like short strings if identical. For runtime variables like s4 a new memory location is located. 
# Thus s1 is s4 results False since memory locations of both the variables are different. 


#String Comparison
s1 = "Python"
s2 = "Java"
print(s1 == s2)  # Output: False
print(s1 != s2)  # Output: True
print(s1 < s2)   # Output: True
print(s1 > s2)   # Output: False

text = "Python is Fun"
result = text.strip().lower().replace(" ","_")
print(result)  # Output: python_is_fun

#Tuple (tuple)#--------------------------------------------------------
coordinates = (10, 20)
new_coords = coordinates
coordinates = coordinates + (30,)  # Creates a new tuple object
print(coordinates)  # Output: (10, 20, 30)
print(new_coords)  # Output: (10, 20)

# Accessing elements
t = (1, 2, 3, 4, 5)
print("First element:", t[0])    # 1
print("Last element:", t[-1])    # 5

#Slice a tuple
t = (1, 2, 3, 4, 5)
print(t[1:4])  # Output: (2, 3, 4)

#tuple concatenation and repetition
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("concatentaion :", t1+ t2)  # Output: (1, 2, 3, 4, 5, 6)
print("Repetation:",  t1 * 2)   # Output: (1, 2, 3, 1, 2, 3)

#tuple in mutability
t2_2 = (1, 2, 3)
#t2_2[0] = 4  # Raises a TypeError: 'tuple' object does not support item assignment
print(t2_2)  # Output: (1, 2, 3)

# Tuple with a mutable list
t = (1, [2, 3], 4)
# Modifying the list inside the tuple
t[1].append(5)
print("Modified Tuple:", t)  # Output: (1, [2, 3, 5], 4)

#convert tuple to list for modification
t = (1, 2, 3)
l = list(t)
print(l)  # Output: [1, 2, 3]

t = (1, 2, 3, 4)
lst = list(t)  
lst[1] = 99  
t = tuple(lst)
print("Modified Tuple:", t) #Output: Modified Tuple: (1, 99, 3, 4)

#Tuple unpacking
t = (1, 2, 3)
a, b, c = t
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

#What is the difference between a list and a tuple in Python?
''' A list and a tuple are both data structures in Python that store a collection of elements. 
The main differences between them are:
Mutability: Lists are mutable, meaning you can change, add, or remove elements after creating the list.
Tuples are immutable, meaning you cannot change, add, or remove elements after creating the tuple.
Syntax: Lists are defined using square brackets [] and tuples are defined using parentheses ().
Performance: Since tuples are immutable, they are faster and more memory-efficient than lists.
Use cases: Use lists when you need a collection of elements that can be modified. Use tuples when you need a collection of elements that should not be modified.
'''

#Frozen Set (frozenset)
frozen_items = frozenset([1, 2, 3])
# Attempting to add to a frozenset raises an AttributeError
try:
    frozen_items.add(4)
except AttributeError as e:
    print(e)  # Output: 'frozenset' object has no attribute 'add'
print(frozen_items)  # Output: frozenset({1, 2, 3})
# Bytes (bytes)

byte_data = b"Hello"
# Attempting to modify bytes directly raises a TypeError
try:
    byte_data[0] = 72
except TypeError as e:
    print(e)  # Output: 'bytes' object does not support item assignment
print(byte_data)  # Output: b'Hello'
'''Each example shows that once these immutable objects are created, any "modification" instead results in a new object being created 
or an error being raised if modification is attempted.'''

#Examples # Bytearray (bytearray)
byte_data = bytearray(b"Hello")
byte_data[0] = 72  # Modifies the first byte
print(byte_data)  # Output: bytearray(b'Hello')

byte_data.extend(b" World")  # Appends more bytes
print(byte_data)  # Output: bytearray(b'Hello World')
'''In each of these examples, the original object is modified directly rather than creating a new object in memory.'''

#List Method operations: ##---------------------------------------------
#1 append(x) - add an item x to end of the list
lst1 = [1, 2, 3, 4, 5, 6, 7] 
lst1_1 =[8,9]
print(lst1, id(lst1)) #Output : [1, 2, 3, 4, 5, 6, 7] 1805575681984
lst1.append(8)
print(lst1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(lst1, id(lst1)) #Output :[1, 2, 3, 4, 5, 6, 7, 8] 1805575681984
lst1.append(lst1_1)
print(lst1) #output [1, 2, 3, 4, 5, 6, 7, 8, [8, 9]]

number  =[10, 20, 30, 40, 50, 60, 70]
print(number[2]) #Output: 30
print(number[0:3])#Output: [10, 20, 30]
print(number[1:4]) #Output: [20, 30, 40]
print(number[-1]) #Output: 70
print(number[-2]) #Output: 60
print(number[-3:]) #Output: [50, 60, 70]
print(number[0:5:2]) #Output: [10, 30, 50]
print(number[::2]) #Output: [10, 30, 50]
print(number[::-1]) #Output: [70, 60, 50, 40, 30, 20, 10]
print(number[::-2]) #Output: [70, 50, 30, 10]
print(number[1:4:2]) #Output: [20, 40]
print(number[::2]) #Output: [10, 30, 50]
print(number[1:4]) #Output: [20, 30, 40]
print(number[::2]) #Output: [10, 30, 50]
print(number[-1::-1]) #Output: [70, 60, 50, 40, 30, 20, 10]
print(number[-1:0:-1]) #Output: [70, 60, 50, 40, 30, 20]

#2 extend(iterable) - extend the list by appending elements from the iterable 
lst2 = [1, 2, 3]
lst2.extend([4, 5])
print(lst2) # Output: [1, 2, 3, 4, 5]
#3 insert(i, x) - inser an item x at given position i
lst3 = [1, 2, 3]
lst3.insert(1,6)
print(lst3) #Output [1, 6, 2, 3]
#4 remove(x) - Removes the first occurance of the item x.
lst4 = [1, 2, 3, 4]
lst4.remove(3)
print(lst4) #Output: [1, 2, 4]
#5 pop([i]) -removes and return the item at the given index i (or the last item if index is not provided )
lst5 = [1, 2, 3, 4]
lst5.pop()
print(lst5) #Output: [1, 2, 3]
#6 clear() - removes all the items
lst6 = [1, 2, 3]
lst6.clear()
print(lst6) #output[]
#7 index(x, [start, [end]]) - return the index of the first occurance of x in the list
lst7 = [1, 2, 3]
print(lst7.index(2)) #Output: 1
#8 count(x) - return the number of occurance of x in the list
lst8 = [1, 2, 4, 5, 5]
print(lst8.count(5)) #Output: 2
#9 sort(key=None, reverse=False) - sort the list inplace (by default in asscending order ).
lst9 = [3, 2, 1]
lst9.sort()
print(lst9) #Output [1, 2, 3]
#10 reverse() - Reverse the list in place
lst10 = [1, 2, 3]
lst10.reverse()
print(lst10)
#11 copy() - return a shallow copy of the list
lst11 = [1, 2, 3]
lst11_copy = lst11.copy()
print(lst11_copy) #Output [1, 2, 3]
#12 len(lst) -return the length of the list 
lst12 = [1, 2, 3]
print(len(lst12)) #output: 3
#13 in check the item is exists in the list
lst13 = [1, 2, 3]
print(3 in lst13)
#14 + -- Concatenates two list 
lsta = [1, 2]
lstb = [3, 4]
lst14 = lsta + lstb
print(lst14) #output [1, 2, 3, 4]
#15 * - repeat the list
lst15 = [1, 4, 6]
print(lst15 * 3) # Output [1, 4, 6, 1, 4, 6, 1, 4, 6]
#16 -netested list
lst166 = [3, 4, 5, 6]
lst166[0] = 4
print(lst166) #output [4, 4, 5, 6]
lst16 = [[1, 2], [3, 4], [5, 6]]
print(lst16[1][0]) #Output 3 
lst16[1][0] = 7
print(lst16) #Output [[1, 2], [7, 4], [5, 6]]
lst16[1].append(9)
print(lst16) #Output [[1, 2], [7, 4, 9], [5, 6]]

#17 List Comprehensions - Useful for creating new lists by transforming data.
squares = [x*x for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
#-------------------------------------------
l_root =[i**2 for i in range(8)][:2]
#print(l_root[4:6]) #Output: []
print(l_root[2:4]) #Output: [4, 9]
#---------------------------------------------------
# List comprehension to filter positive numbers only 
numbers = [-10, 4, 6, 8, -12]
positive_numbers = [n for n in numbers if n > 0] 
print(f"Posttive numbers: {positive_numbers}") # Output: Positive numbers: [4, 6, 8]
#--------------------------------------------------------------------
L = [1, 2, 3, 4, 5]
a = L
a[2] = 42
print(L)  # [1, 2, 42, 4, 5]
print(a) # [1, 2, 42, 4, 5]

#how to get range argument from list?
args = [2, 10, 2]   # start=2, stop=10, step=2
for i in range(*args):
    print(i)  # Output: 2, 4, 6, 8
#list.index(value) is used to find the position (index) of a value in a list.
nums = [10, 20, 30, 20]
nums.index(20)
nums.index(20, 2)   # start searching from index 2
nums.index(20, 1, 3)  # search between index 1 and 2
#----------------------------
a = [1]
b = a
b += [2]
b.append(3)
b = b + [4] #b = b + [4] creates a new list object and assigns it to b, while a still references the original list. 
b.append(5)
print(a)  # Output: [1, 2, 3]  
print(b)  # Output: [1, 2, 3, 4, 5]
#--------------------------------------------------
l1 = ["Mu", "Ve", "Ea", "Ma"]
l2 = ["Eg", "Pa", "Ca"]
l1.append(l2.append(l1[2])) or l2.pop(1) if len(l1)>3 and len(l2) > 1 else l2.remove(l2[9]) 
        #Step1 to check if condition and then step2 to execute the operation
print(l1) #Output: ['Mu', 'Ve', 'Ea', 'Ma', None]

#Dictionary Method operations:
#1 dict.clear() - remove all the item from dictionary 
d1 = {'a': 1, 'b': 2}
d1.clear()
print(d1) #output {}
#2 dict.copy() -returns a shallow copy of the dictionary 
d2 = {'a': 1, 'b': 2}
d_copy = d2.copy()
print(d_copy) #output {'a': 1, 'b': 2}
#3 dict.get(key , default= None) - return the value for key if key is in the dictionary , otherwise return default.
d3 = {'a': 1, 'b': 2}
print(d3.get('a')) # output 1
print(d3.get('c', 0)) #output 0
print(d3['a']) # output 1

#4 dict.items() - returns a view object that displays a list of dictionary's key-value tuple pair
d4 = {'a': 1, 'b': 2}
print(d4.items()) # output dict_items([('a', 1), ('b', 2)])
#5 dict.keys - return the view of object that display a list of all the keys in the dictionary
d5 = {'a': 1, 'b': 2}
print(d5.keys()) # output: dict_keys(['a', 'b'])
#6 dict.values() return the view of object that display a list of all the values in the ddictionary
d6 = {'a': 1, 'b': 2}
print(d6.values()) #output: dict_values([1, 2])
#7 dict.pop(key, default= None) Removes the specific key and returns the corrspending value. if the key is not found returns defult.
d7 = {'a': 1, 'b': 2}
value = d7.pop('a') #empty pop() with through the error 
print(value) # output 1
print(d7) #output {'b': 2}
#8 dict.popitem() -reomve and return the last element key-value pair as tuple
d8 = {'a': 1, 'b': 2}
item = d8.popitem() 
print(item) #output (b, 2)
print(d8) # output {'a', 1}
#9 dict.update(iterable) - update the dictionary with element from another dictionary 
d9 = {'a': 1, 'b': 2}
d9.update({'b': 4, 'c': 7})
print(d9) #Output {'a': 1, 'b': 4, 'c': 7}
#10 dict.setdefault(key, default=None) -Returns the value of key if it is in the dictionary if not insert key with a value of default
d10 = {'a': 1}
value = d10.setdefault('b', 3)
print(value) #output 3
print(d10) #output {'a': 1, 'b': 3}

d10_1= {'Jade':1, 'John':2, 'Jame':3}
keys = ['John', 'Jacob', 'Jake']
values = [4, 5, 6]
for key, value in zip (keys, values):
    d10_1.setdefault(key, value)
print(d10_1) #Output: {'Jade': 1, 'John': 2, 'Jame': 3, 'Jacob': 5, 'Jake': 6}

#11 dict.fromkeys(iterable, value=None) - Creates a new dictionary with keys from iterable and values set to value.
keys = ['a', 'b', 'c']
d11 = dict.fromkeys(keys, 0)
print(d11)  # Output: {'a': 0, 'b': 0, 'c': 0}
#12 Accessing values by keys
d12 = {'a': 1, 'b': 2}
print(d12['a'])  # Output: 1
#13 Using in to check if a key exists
d13 = {'a': 1, 'b': 2}
print('a' in d13)  # Output: True

#Merging two dictionaries If both dictionaries have the same key
d13_1 = {'a': 1, 'b': 2}
d13_2 = {'c': 3, 'd': 4}
d13_1.update(d13_2)
print(d13_1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
merged = d13_1 | d13_2
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#---------------------------
dict13_3 = {'a': 1, 'b': 2}
dict13_4 = {'b': 3, 'c': 4}
dict13_3.update(dict13_4)
print(dict13_3)  # Output: {'a': 1, 'b': 3, 'c': 4}
print(dict13_3 | dict13_4)  # Output: {'a': 1, 'b': 3, 'c': 4}
print({**dict13_3, **dict13_4})  # Output: {'a': 1, 'b': 3, 'c': 4}
#-------------------------------------------------------------------------------
dict13_5 =['aa', 'bb' ]
dict13_6 = [1,2]
dict13_5_6 = dict.fromkeys(dict13_5, dict13_6)
print(dict13_5_6) #Output: {'aa': [1, 2], 'bb': [1, 2]}

#14 Dictionary Comprehensions - Useful for creating new dictionaries by transforming data.
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

root = {x**2:x for x in range(8, 0, -1)} 
print ("Method 2 Using Lis Comperheshion", root) #Output: {64: 8, 49: 7, 36: 6, 25: 5, 16: 4, 9: 3, 4: 2, 1: 1}

# Initial dictionary
person = {"name": "John", "age": 25}
person["age"] = 26
person.update({"city":"New York"})
del person["name"]    # Delete the 'name' key
print(person) #Output: {'age': 26, 'city': 'New York'}

#15 Dictionary sorting
my_dict = {3:"Deepak", 1:"UST", 5:"HCL", 2:"Python", 4:"bosch"}

# Sort by keys (ascending)
sorted_by_keys = dict(sorted(my_dict.items()))
print("Sorted by keys (ascending):", sorted_by_keys) 
#Sorted by keys (ascending): {1: 'UST', 2: 'Python', 3: 'Deepak', 4: 'bosch', 5: 'HCL'}
# Sort by keys (descending)
sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
print("Sorted by keys (descending):", sorted_by_keys_desc)
#Sorted by keys (descending): {5: 'HCL', 4: 'bosch', 3: 'Deepak', 2: 'Python', 1: 'UST'}
# Sort by values (ascending)
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by values (ascending):", sorted_by_values)
#Sorted by values (ascending): {3: 'Deepak', 5: 'HCL', 2: 'Python', 1: 'UST', 4: 'bosch'}
# Sort by values (descending)
sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by values (descending):", sorted_by_values_desc)
#Sorted by values (descending): {4: 'bosch', 1: 'UST', 2: 'Python', 5: 'HCL', 3: 'Deepak'}

# Nested Dictionary
nested_dict = {'person1': {'name': 'Alice','age': 25,'address': {'city': 'New York','zipcode': '10001'}},
               'person2': {'name': 'Bob','age': 30,'address': {'city': 'Los Angeles', 'zipcode': '90001'}}}
# Access 'name' of 'person1'
print(nested_dict['person1']['name'])  # Output: Alice
# Access 'city' of 'person2'
print(nested_dict['person2']['address']['city'])  # Output: Los Angeles
# Update 'age' of 'person1'
nested_dict['person1']['age'] = 26
# Add a new key-value pair to 'person2'
nested_dict['person2']['phone'] = '555-1234'
print(nested_dict)

dct = {1: "deepak", 2: ["3", {5:"Few"}], 3: {4: "python"}}
print(dct[1])  # Output: deepak
print(dct[2])  # Output: ['3', {5: 'Few'}]
print(dct[2][0])  # Output: 3
print(dct[2][1][5]) #Output: Few
print(dct[3])  # Output: {4: 'python'}
print(dct[3][4])  # Output: python
#---------------------------------------
data = {"old_key": "value"}
# change key
data["new_key"] = data.pop("old_key")
print(data) #Output: {'new_key': 'value'}
#----------------------------------------------------
pd1 = {'book': 10, 'apple': 20, 'vechile': {'car': 5, 'bike': 12}}
pd2 = pd1.copy() 
print(pd2) #Output: {'book': 10, 'apple': 20, 'vechile': {'car': 5, 'bike': 12}}
pd1.clear()
print(pd1) #Output: {}

#SET Method operations:
#1 add(element) - Adds an element to the set.
s1= {1, 2, 3}
s1.add(4)
print(s1) #output {1, 2, 3, 4}
print(2 in s1) #Output : True
print(len(s1)) #output : 4
s1_items ={"apple", "banana", "apple"}
print(s1_items) #Output : {'banana', 'apple'}

#2 clear() Removes all elements from the set.
s2 = {1, 2, 3}
s2.clear()
print(s2)  # Output: set()
#3 copy() - Returns a shallow copy of the set.
s3 = {1, 2, 3}
s_copy = s3.copy()
print(s_copy)  # Output: {1, 2, 3}
#4 pop() -Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
s4 = {1, 2, 3}
element = s4.pop()
print(element)  # Output: 1 (or another random element)
print(s4)
fruits = {"apple", "banana", "cherry"}
x = fruits.pop() 
print(x)
print(fruits)
#5 remove(element) - Removes a specific element from the set. Raises KeyError if the element is not found.
s5 = {1, 2, 3}
s5.remove(2)
print(s5)  # Output: {1, 3}
#6 discard(element) - Removes a specific element if it is a member of the set. Does nothing if the element is not found.
s6 = {1, 2, 3}
s6.discard(2)
print(s6)  # Output: {1, 3}
#7 union(*others) - Returns a new set with elements from the set and all other sets.
s7_1 = {1, 2, 3}
s7_2 = {3, 4, 5}
result7 = s7_1.union(s7_2)
print(result7)  # Output: {1, 2, 3, 4, 5}
#8 update(*others)- Updates the set, adding elements from all other sets.
s8 = {1, 2, 3}
s8.update({3, 4, 5})
print(s8)  # Output: {1, 2, 3, 4, 5} here set s8 will stay unchanged 
#9 intersection(*others) - Returns a new set with elements common to the set and all others.
s9_1 = {1, 2, 3}
s9_2 = {2, 3, 4}
result9 = s9_1.intersection(s9_2)
print(result9)  # Output: {2, 3}
#10 intersection_update(*others) - Updates the set, keeping only elements found in it and all others.
s10 = {1, 2, 3}
s10.intersection_update({2, 3, 4})
print(s10)  # Output: {2, 3}
#11 difference(*others) - Returns a new set with elements in the set that are not in the others.
s11_1 = {1, 2, 3}
s11_2 = {2, 3, 4}
result11 = s11_1.difference(s11_2)
print(result11)  # Output: {1}
#12 difference_update(*others) - Updates the set, removing elements found in others.
s12 = {1, 2, 3}
s12.difference_update({2, 3})
print(s12)  # Output: {1}
#13 symmetric_difference(other) - Returns a new set with elements in either the set or other but not both.
s13_1 = {1, 2, 3}
s13_2 = {2, 3, 4}
result13 = s13_1.symmetric_difference(s13_2)
print(result13)  # Output: {1, 4}
#14 symmetric_difference_update(other) - Updates the set, keeping only elements found in either set, but not in both.
s14 = {1, 2, 3}
s14.symmetric_difference_update({2, 3, 4})
print(s14)  # Output: {1, 4}
#15 issubset(other) - Returns True if the set is a subset of other.
s15_1 = {1, 2}
s15_2 = {1, 2, 3}
print(s15_1.issubset(s15_2))  # Output: True
#16 issuperset(other) - Returns True if the set is a superset of other.
s16_1 = {1, 2, 3}
s16_2 = {1, 2}
print(s16_1.issuperset(s16_2))  # Output: True
#17 isdisjoint(other) - Returns True if the set has no elements in common with other.
s17_1 = {1, 2}
s17_2 = {3, 4}
print(s17_1.isdisjoint(s17_2))  # Output: True

s18 = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(s18))  # Convert to set and back to list to remove duplicates
print(unique)  # Output: [1, 2, 3, 4, 5]
s19 = {1, 2, "abc"}
s19.add((1, 2, 3)) #[] list unhasable 
print(s19)  #() hasble

#Set Comprehensions -Useful for creating sets with specific conditions.
squares = {x**2 for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}

my_list = [1, 2, 3]
my_tup = (4, 5, 6)
my_dict = {'a': 7, 'b': 8, 'c': 9}
my_set = {10, 11, 12}
print(len(my_list)+ len(my_tup)+ len(my_dict)+ len(my_set)) #Output : 12
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: HOW TO CONVERT TWO LIST INTO A DICTONARY 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
keys = ["name", "age", "city"]
values = ["Dipu", 32, "Blore" ]

my_dict = {keys[i]: values[i] for i in range(len(keys))}

my_dict2 = dict.fromkeys(keys,values)

print(my_dict)
print(my_dict2)

color = ["orage", "pink", "black"]
qty = [3, 4, 5]
res33 = zip(color, qty)
print(res33, type(res33)) #Output : <zip object at 0x000001A4646B1980> <class 'zip'>
res33= dict(zip(color, qty))
print(res33, type(res33)) #Output : {'orage': 3, 'pink': 4, 'black': 5} <class 'dict'>

color1 = ["orage", "pink", "black", "orage"]
qty1 = [3, 4, 5, 7]  #zip both the list and convert to dictionary, it added "Orange" as one key but in stead of adding two of the quantities i.e. 2+5 = 7 it took only the latest value i.e. 5
res34= dict(zip(color1, qty1))
print(res34, type(res33)) #Output: {'orage': 7, 'pink': 4, 'black': 5} <class 'dict'>

a = [1, 2, 3]
b = [4, 5, 6]
total = [x + y for x, y in zip(a, b)]
print(total)  # Output: [5, 7, 9]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a = [1, 2, 3, 4, 5, 6]
b = a[1:3]
b[0] = 0
print (a)
print (b)

x2 = [4, 5]
x2 += [6, 7]
print(x2)  # Output: [4, 5, 6, 7]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: How to Display the elements in dictionary ?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Method 1 Display keys and values 
my_dict_q3 = {'name': 'robo', 'age': 24, 'city': 'blr'}
for key, value in my_dict_q3.items(): # Display each key and value
    print(f"{key} : {value}")

# Method 2 Display only keys
for key in my_dict_q3.keys():
    print(key)

# Method 3 Display only values
for value in my_dict_q3.values():
    print(value)

# Method 4 display keys and values using item()
for item in my_dict_q3.items():
    print(item)

# Method 5 dictionary to String and Display
print(str(my_dict_q3))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Convet a string to dictinoary "hello=world, world=is, is=he" using split ans strip
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
input_string = "hello=world, world=is, is=he"
pairs = input_string.split(",")
result_dict = {}
for pair in pairs:
    key, value = pair.split("=")
    result_dict[key.strip()] = value.strip()
print(result_dict)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a5 = [1, 2, 3]
b5 = [x, y]
res5 = list(zip(a5, b5))
print(res5) #Output [(1, 'x'), (2, 'y')]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
statement = "I am a software engineer"
lst = statement.split()
print(lst, type(lst)) # Output : ['I', 'am', 'a', 'software', 'engineer'] <class 'list'>


color2 = ["orage", "pink", "black", "orage"]
res = "".join(color2)
print(res, type(res)) #Output : oragepinkblackorage <class 'str'>
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Write a function to flatten a nested list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def flatten(f_lst):
    result = []
    for i in f_lst: 
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
f_lst = [1, [2, 3], [4, [5, 6]], 7]
print(flatten(f_lst))  # Output: [1, 2, 3, 4, 5, 6, 7]
f_lst_1 = [1, [2, 3], [4, [5, 6]], 7]
flattened = [item for sublist in f_lst_1 for item in (sublist if isinstance(sublist, (list, tuple)) else [sublist])]
print(flattened)

nest_lst = [["Alice", 25],["Bob", 30],["Charlie", 22]]
def flatten_iter(lst):
    stack = [iter(lst)]
    result = []
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                result.append(item)
        except StopIteration:
            stack.pop()
    return result
print(flatten_iter(nest_lst))
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
data = {}
items = [('a', 1), ('b', 2), ('a', 3)]
for key, value in items:
    if key not in data:
        data[key] = []
        data[key].append(value)
# Genius way
data = {}
for key, value in items:
    data.setdefault(key, [] ).append(value)
# Output: {'a': [1, 3], 'b': [2]}

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import copy
mydict = {1: [], 2: [], 3: []}
c1 = mydict
c2 = mydict.copy()
c3 = copy.deepcopy (mydict)
c1 [1].append(100)
c2 [2].append(200)
c3 [3].append (300)
print(mydict)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def func(a):
    a[0] = 2
    return a   # or return x? but x is the original list # here x wiil assgin give type error 
x = [1, 2, 3]   # list instead of  x = (1, 2, 3) tuple
print(func(x))  # Output: [2, 2, 3] 

def fun(num, ls =[]):
    ls.append(num)
    return ls
print(fun(1))


temp = 20  # Global variable
def funct():
    temp = 40  # Local variable, shadows the global variable
    print(temp)  # Prints the local temp value (40)
    print(temp)  # Prints the local temp value (40)

funct()  # Calls the function, executing its code
print(temp)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
ip1 = "10.45.123.1:5004"
# Split into IP and Port
ip_addr, port = ip1.split(":")
print("IP Address:", ip_addr)
print("Port:", port)

ip2 = "10.45.123.1:5004"
ip_addr, port = ip2.split(":")
oct1, oct2, oct3, oct4 = ip_addr.split(".")
print("Octet 1:", oct1)
print("Octet 2:", oct2)
print("Octet 3:", oct3)
print("Octet 4:", oct4)
print("Port:", port)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: WAP to find the first element inlist if it found stop the  loop.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
current = 0
for p in pat:
    if p == 0:
        current = p
        break
    elif p % 2 == 0:
        continue
    print(p)
print(current)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: From string find the word
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
deloite = "deloite Interview@2026"
st =""
for char in deloite:
    if char.isalpha():
        st += char
print(st)   #Output 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: WAP to make each alternative charter capitalization in string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#s = input("Enter name: ")
# Capitalize first and last character of each word
ivtechm1 = "TECH MAHINDRA IBM"
words = ivtechm1.split()
result = []
for word in words:
    word = word.lower()
    if len(word) > 1:
        new_word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        new_word = word.upper()
    result.append(new_word)
print(" ".join(result)) # Output: TecH MahindrA IbM

###Alternate character capitalization
ivtechm2 = "TECH MAHINDRA IBM CLIENT"
res_alt = ""
for i in range(len(ivtechm2)):
    if i % 2 == 0:
        res_alt += ivtechm2[i].upper()
    else:
        res_alt += ivtechm2[i].lower()
print(res_alt) # Output: TeCh mAhInDrA IbM ClIeNt
  
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 ::  WAP Reverse whole string and Capitalize first letter of each word
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
ivtechm3 = "Tech Mahindra interview ibm"
rev_itm = ivtechm3[::-1]   # Step 1: reverse string
result = []     # Step 2: capitalize each word
for word in rev_itm.split():
    result.append(word.capitalize())
print(" ".join(result)) #Output: Mbi Weivretni Ardniham Hcet

print(" ".join(word.capitalize() for word in ivtechm3[::-1].split())) #Output: Mbi Weivretni Ardniham Hcet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
