# return :== the return keyword ends the function and send the result back to the place where the function was called.
# *arg :== to pass available number of positional arguments, collect extra positional argument into tuple
# function :== A function is a block of code that perfrms a specific task and can be reused.
from ast import Yield
import sys
data_list = [1, 2, 3, 4, 5]
data_tuple = (1, 2, 3, 4, 5)
data_set = {1, 2, 3, 4, 5}
data_string = "12345"
print("List memory:", sys.getsizeof(data_list)) #List memory: 104
print("Tuple memory:", sys.getsizeof(data_tuple)) #Tuple memory: 88
print("Set memory:", sys.getsizeof(data_set)) #Set memory: 472
print("String memory:", sys.getsizeof(data_string)) #String memory: 46 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 0 :: Why python is called as interpreted language?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
✅Compiler vs Interpreter
Both are used to convert high-level programming language into machine code, but they work differently.
Compiler:
1. Translates the entire source code into machine code before execution.
2. Generates an executable file that can be run independently.
3. Errors are detected after the compilation process, and the program won't run until all errors are fixed.
        Process :::    Source Code → Compiler → Executable File → Run
        Ex: Translating entire book before reading
Interpreter:
1. Translates and executes the source code line by line.
2. Does not generate an executable file; it directly executes the code.
3. Errors are detected immediately when the line of code is executed, allowing for quicker debugging.
        Process :::    Source Code → Interpreter → Execute Line-by-Line
        Ex: Translating sentence-by-sentence while speaking
        first compiles to bytecode and then Python Virtual Machine (PVM) interprets it
        .py → bytecode (.pyc) → PVM executes


✅.py vs .pyc File in Python
    ✅ .py File
        A .py file contains:    Human-readable Python source code which file that developers write and edit


    ✅ .pyc File
        A .pyc file contains:   Compiled Python bytecode executed by the Python Virtual Machine (PVM)
        Location
            Usually inside:
                __pycache__/
            Example:
                __pycache__/
                    hello.cpython-312.pyc

Python Execution Flow
.py file
   ↓
Python Compiler
   ↓
.pyc bytecode
   ↓
Python Virtual Machine (PVM)
   ↓
Execution

the folder containing __init__.py indicates that the folder will be considered a package.
let's break it down
bit > numbers > characters > instructions > function > program > modules > packages > library > frameworks > software
!!!!! >>> >>> >>> instruction are single line of code that represent an operation to be preform by a computer prossor.

Questions 1 :: What is the difference between a Module and a Package?
Module: A single file containing Python code (functions, classes, variables) ending in .py.
Package: A directory containing multiple modules and an __init__.py file.

Questions 2 :: What is the difference between *args and **kwargs?
*args: Collects extra positional arguments as a tuple.
**kwargs: Collects extra keyword arguments as a dictionary.
'''
args = [2, 10, 2]   # start=2, stop=10, step=2
for i in range(*args):
    print(i) #Output: 2, 4, 6, 8
#----------------------------------------------
params = [0, 20, 5]
r = range(*params)
print(list(r))  # [0, 5, 10, 15]

pairs = [(1, 'a'), (2, 'b')]
nums, chars = zip(*pairs)
print(nums)   # (1, 2)
print(chars)  # ('a', 'b')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: What is the difference between deep and shallow copy?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#1. Shallow Copy: both the list change Changing an inner list in original affects shallow_copied as well
import copy
original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

# Modify the original
original[0][0] = 100

print("Original:", original)  # Output: [[100, 2, 3], [4, 5, 6]]
print("Shallow Copy:", shallow_copied)  # Output: [[100, 2, 3], [4, 5, 6]]
#2. Deep Copy: only coied list change changes to the original object do not affect the deep copy. The inner lists are new instances, 
import copy
original1 = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original1)

# Modify the original
original1[0][0] = 100

print("Original:", original1)  # Output: [[100, 2, 3], [4, 5, 6]]
print("Deep Copy:", deep_copied)  # Output: [[1, 2, 3], [4, 5, 6]]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: What is pickling and un-pickling? 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Pickling:
#Pickling is the process of converting a Python object into a byte stream (a serialized form). This allows objects like lists, dictionaries, and even custom Python objects to be stored in files or sent over a network.
import pickle

# Data to be pickled
my_data = {"name": "Alice", "age": 25, "city": "New York"}

# Pickle the data to a file
with open("data.pkl", "wb") as file:
    pickle.dump(my_data, file)
#Unpickling:
#Unpickling is the reverse process: it takes the byte stream produced by pickling and converts it back into a Python object.

import pickle

# Unpickle the data from the file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: What is generator? with example
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#A generator in Python is a special type of iterator that allows you to iterate over a sequence of values.'
#Yield
# yield is used to create a generator in Python. Instead of returning all values at once, 
# it pauses the function and returns values one by one.
# Produces values
#Used inside generator function
#NEXT
# next() is used to retrieve the next value from that generator and resume execution from where it stopped.
#Consumes values
#Used outside generator
def generators():
    for i in range(23):
        yield i       
g = generators()
print(next(g))

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
# Create a generator
counter = count_up_to(5)
# Iterate through the generator
for num in counter:
    print(num)
###########    
def countdown(n):
    while n>0:
        yield n
        n -= 1
for num1 in countdown(3):
    print("num1", num1)
#############
def evens(n):
    for i in range(n +1):
        if i % 2 ==  0:
            yield i

# Calling generator using a loop (standard way)
print("--- Using a for loop ---")
for even in evens(9):
    print("even", even)

# Using next() function (manual iteration)
print("\n--- Using next() function ---")
gen_manual = evens(9) # Create a fresh generator specifically for next() calls

print(next(gen_manual))  # 0
print(next(gen_manual))  # 2
print(next(gen_manual))  # 4
print(next(gen_manual))  # 6
print(next(gen_manual))  # 8

# If you run print(next(gen_manual)) now, it raises StopIteration

# How is a generator different from a list ?
# generator doesnt store all value in memory .they compute value on the fly. mKING THEM IDEAL FOR LARGE DATA SETS OR INFINITE SEQENCE 

#Example: Fibonacci Sequence Using a Generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# Create a generator
fib = fibonacci()
# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib))
        
#Generator Expressions:
#Similar to list comprehensions, Python has generator expressions that allow you to create generators in a more concise manner.
# List comprehension
squares = [x * x for x in range(10)]

# Generator expression
squares_gen = (x * x for x in range(10))

# Using the generator
for square in squares_gen:
    print(square)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Sum of argument
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def add_number(*args):
    return sum(args)
print(add_number(1, 2, 3, 4)) #OutPut = 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Write a program to take an array of integers as input and calculate the sum of all elements in the array.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [5, 10, 15, 20, 25]
print("Sum of elements:", sum_of_elements(arr))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Write a program to find the maximum and minimum values in an array of integers.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def find_max_min(arr):
    maximum = arr[0]
    minimum = arr[0]
    
    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum
# Example input
arr = [5, 10, 15, 20, 25]
max_val, min_val = find_max_min(arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Write a program to search for an element in an array and return its index. If the element is not found, display a message.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def search_element(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        return -1  # Element not found
# Example input
arr = [10, 20, 30, 40, 50]
target = 40 #int(input("Enter the element to search: "))
# Search and display result
index = search_element(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array.")
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Python - split string on vowels
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def split_str(inp):
    vowels = "aeiouAEIOU"
    lst = []
    crr_str = ""
    for char in inp:
        if char in vowels:
            if crr_str:
                lst.append(crr_str)
                crr_str =""
        else:
            crr_str +=char
    if crr_str:
        lst.append(crr_str)
    return lst
inp = "GFGaBsf"
print(split_str(inp))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: mutable default arguments
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def lst_n(s,t=[]):
    t.append(s)
    return t
print(lst_n(1))
print(lst_n(2))
print(lst_n(3, []))
print(lst_n(4))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: and operator short-circuits logic
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 10
y = 50
if x**2 > 100 and y < 100:
    print("Yes")
else:
    print("No")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: nested Dictionary operation to data
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
data = {"jens": ["python", "visual studio"],"sara's": ["storage"],"phili's": ["python", "c++"]}
for name, languages in data.items():
    print(f"{name} favorite language {' '.join(languages)}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: string operation
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
s = "how old are you ? 54"
for word in s.split():
    if word.isdigit():
        print("deepak", word, "years old")
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Write a program to find the elements between two lists and return them as a new list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def process_list(l1):
    l1=[num for num in range (1,11)]
    l1[3] = [i for i in l1 if not i % 3][2] #Output: 9
    l2 = [i for i in range(20) if not i % 5] #Output: [0, 5, 10, 15, 20, 25]
    l2.extend(l1)
    print(l2) #Output: [0, 5, 10, 15, 20, 25, 1, 2, 3, 9, 5, 6, 7, 8, 9, 10]
    return l2[::2]
print(process_list()) #Output: [0, 10, 20, 1, 3, 5, 7, 9]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Write a program to flatten a nested or matrix list/array.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
new_matrix = sum(matrix1, [])
print(new_matrix) #Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: What is the difference between deep and shallow copy?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''