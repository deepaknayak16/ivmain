
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i)) # str will print the string way of the number
print(l)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
n = 8
print(factorial(n))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral 
number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 8
d = dict()
for i in range(1, x + 1):
    d[i] = i * i
print(d)
#---method-2 -----#
q3 = {i: i * i for i in range(1, 9)}
print(q3)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 ::Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains 
every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q4 = input("Enter the numbers: ")
l = q4.split(",")
t = tuple(l)
print(l)
print(t)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class String:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())
obj = String()
obj.getString()
obj.printString()


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from collections import Counter
import math
int1 = "100,150,180"
c = 50
h = 30
value = []
items = [x for x in int1.split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2 * c * int(d) / h)))))
print(','.join(value))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and 
j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q7 = "3,5" #input("Enter the numbers: ") 
x, y = map(int, q7.split(",")) # 3,5
l = [[0 for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        l[i][j] = i * j
print(l)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q8 = "without,hello,bag,world"
l = q8.split(",")
l.sort()
print(",".join(l))
#method2
# Implementing a simple bubble sort algorithm
for i in range(len(l)):
    for j in range(0, len(l) - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print(",".join(l))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# q9 = []
# while True:
#     s = "Hello world Practice makes perfect"
#     if s:
#         q9.append(s.upper())
#     else:
#         break 
# for sentence in q9:
#     print(sentence)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q10 = "hello world and practice makes perfect and hello world again"
l10 = q10.split(" ")
print(" ".join(sorted(list(set(l10)))))
#method2 Buble sort and merger sort unique element
unique_words = []
for word in l10:
    if word not in unique_words:
        unique_words.append(word)

# Implementing a simple bubble sort algorithm
for i in range(len(unique_words)):
    for j in range(0, len(unique_words) - i - 1):
        if unique_words[j] > unique_words[j + 1]:
            unique_words[j], unique_words[j + 1] = unique_words[j + 1], unique_words[j]

print(" ".join(unique_words))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 11 :: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

q11 = "0100,0011,1010,1001"
l11 = q11.split(",")
for i in l11:
    if int(i, 2) % 5 == 0:
        print(i)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q12 = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        q12.append(s)
print(",".join(q12))


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q13 = "hello world! 123"
d = {"DIGITS": 0, "LETTERS": 0}
for i in q13:
    if i.isdigit():
        d["DIGITS"] += 1
    elif i.isalpha():
        d["LETTERS"] += 1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 14 :: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q14 = "Hello world!"
d = {"UPPER CASE": 0, "LOWER CASE": 0}
for i in q14:
    if i.isupper():
        d["UPPER CASE"] += 1
    elif i.islower():
        d["LOWER CASE"] += 1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 15 :: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a = 9
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 16 :: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
q16 = "1,2,3,4,5,6,7,8,9"
l16 = q16.split(",")
l16 = [str(int(i) ** 2) for i in l16 if int(i) % 2 != 0]
print(",".join(l16))

# q16 = 1,2,3,4,5,6,7,8,9
# #l16 = q16.split(",")
# l16 = [i ** 2 for i in q16 if i % 2 != 0]
# print(",".join(l16))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 17 :: Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
netamount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netamount += amount
    elif operation == "W":
        netamount -= amount
    else:
        pass
print(netamount)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
q18 = "ABd1234@1,a F1#,2w3E*,2We3345"
l18 = q18.split(",")
accepted = []
for i in l18:
    if len(i) < 6 or len(i) > 12:
        continue
    elif not re.search("[a-z]", i):
        continue
    elif not re.search("[0-9]", i):
        continue
    elif not re.search("[A-Z]", i):
        continue
    elif not re.search("[$#@]", i):
        continue
    else:
        pass
    accepted.append(i)
print(",".join(accepted))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 19 :: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
data = []
while True:
    try:
        line = input()
        if not line:
            break
        name, age, score = line.split(",")
        data.append((name, int(age), int(score)))
    except:
        break
data.sort(key=lambda x: (x[0], x[1], x[2])) # Sort by name, then age, then score
print(data)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 20 :: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reversed(range(100)):
    print (i)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 21 :: DWrite a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
freq = {}   # frequency of words in text
line = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
for word in line.split():
    freq[word] = freq.get(word,0)+1
    
words = freq.keys()
words = sorted(words)
for w in words:
    print ("%s:%d" % (w,freq[w]))
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 22 :: Define a class, which have a class parameter and have a same instance parameter.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Person:
    name = "Person"
    def __init__(self, name = None):
        self.name = name
        
jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 23 :: Define a function that can convert a integer into a string and print it in console.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printValue(n):
    print(str(n))
printValue(3)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 24 :: Define a function that can convert a integer into a string and print it in console.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printValue(n):
    print(str(n))
printValue(3)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 25 :: Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printValue(s1, s2):
    print(int(s1) + int(s2))
printValue("3", "4")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 26 :: Define a function that can accept two strings as input and concatenate them and then print it in console.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printValue(s1, s2):
    print(s1 + s2)
printValue("3", "4")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 27 :: Define a function that can accept two strings as input and print the string with maximum length
in console. If two strings have the same length, then the function should print al l strings line by line.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printValue(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        print(s1)
    elif l1 < l2:
        print(s2)
    else:
        print(s1)
        print(s2)
printValue("one", "three")
printValue("one", "two")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 28 :: Define a function that can accept an integer number as input and print the "It is an even number" 
if the number is even, otherwise print "It is an odd number"
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def evenOdd(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
evenOdd(2)
evenOdd(3)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 29 :: Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and 
the values are square of keys.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printDict():
    d = dict()
    for i in range(1, 4):
        d[i] = i**2
    print(d)
printDict() #OutPut {1: 1, 2: 4, 3: 9}


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 30 :: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the 
values are square of keys. The function should just print the values only.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printDict():
    d = dict()
    for i in range(1, 21):
        d[i] = i**2
    for k in d.values():
        print(k)
printDict()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 31 :: Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and 
the values are square of keys. The function should just print the keys only.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printDict():
    d = dict()
    for i in range(1, 21):
        d[i] = i**2
    for k in d.keys():	
        print(k)
printDict()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 32 :: Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l)
printList()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 33 :: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l[:5])
printList()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 33 :: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l[-5:])
printList()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 34 :: Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l[5:])
printList()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 35 :: Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def printTuple():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(tuple(l))
printTuple()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 36 :: With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half 
values in one line.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
tp = (1,2,3,4,5,6,7,8,9,10)
l = len(tp)
print(tp[:l//2])
print(tp[l//2:])
#method2
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 37 :: Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
tp = (1,2,3,4,5,6,7,8,9,10)
tp1 = tuple(i for i in tp if i%2 == 0)
print(tp1)

tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print (tp2)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 38 :: Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = "yes"
if l == "yes" or l == "YES" or l == "Yes":
    print("Yes")
else:
    print("No")


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 39 :: Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = [1,2,3,4,5,6,7,8,9,10]
l = list(filter(lambda x: x%2==0, l))
print(l)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 40 :: Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = list(map(lambda x: x**2, li))
print (squaredNumbers)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 41 :: Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = [1,2,3,4,5,6,7,8,9,10]
l = list(map(lambda x: x**2, filter(lambda x: x%2==0, l)))
print(l)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 42 :: Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = list(filter(lambda x: x%2==0, range(1,21)))
print(l)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 43 :: Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def sqr(n):
    return n*n
l = list(map(sqr, range(1, 21)))
print(l)

squaredNumbers = list(map(lambda x: x**2, range(1,21)))
print (squaredNumbers)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 44 :: Please raise a RuntimeError exception.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# raise RuntimeError('something wrong')
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 45 :: Write a function to compute 5/0 and use try/except to catch the exceptions.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except Exception as err:
    print("Any other exception")
finally:
    print("This code will run no matter what")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 46 :: Define a custom exception class which takes a string message as attribute.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
num = int(8)
try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 47 :: Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the 
company name of a given email address. Both user names and company names are composed of letters only.
please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
email = "deepaknayak@google.com"
pattern = "(\w+)@(\w+)\.(com)"
r = re.match(pattern, email)
print(r.group(2))

pattern = "(\w+)@((\w+\.)+(com))"
r = re.match(pattern, email)
print(r.group(1))


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 48 :: Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
s = "2 cats and 3 dogs."
print(re.findall("\d+", s))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 49 :: Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
n = 5
sum = 0.0
for i in range(1, n+1):
    sum += float(float(i)/(i+1))
print(sum)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 50 :: Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=10
values = []
for i in even(n):
    values.append(str(i))
print(",".join(values))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 51 :: Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma 
separated form while n is input by console.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def num(n):
    for i in range(n+1): 
        if i%5==0 and i%7==0:
            yield i
n = 10
values = []
for i in num(n):
    values.append(str(i))
print(",".join(values))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 52 :: Please write assert statements to verify that every number in the list [2,4,6,8] is even.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for num in [2, 4, 6, 8]:
    assert num % 2 == 0, f"{num} is not an even number"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 53 :: Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, the element was not present
    return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 54 :: Please generate a random float where the value is between 10 and 100 using Python math module.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.random()*100)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 55 :: Please generate a random float where the value is between 5 and 95 using Python math module.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.random()*100-5)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 56 :: Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.choice([i for i in range(11) if i%2==0]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 57 :: Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 58 :: Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.sample(range(100, 201), 5))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 59 :: Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 60 :: Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 61 :: Please write a program to randomly print a integer number between 7 and 15 inclusive.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random
print(random.randint(7, 15))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 62 :: Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 63 :: Please write a program to print the running time of execution of "1+1" for 100 times.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from timeit import Timer
t = Timer("for i in range(100):1+1")
print (t.timeit())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 64 :: Please write a program to shuffle and print the list [3,6,7,8].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 65 :: Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 66 :: Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print (li)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
li = [12,24,35,70,88,120,155]
li = [x for x in li if x % 5 != 0 and x % 7 != 0]
print (li)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print (li)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = [12,24,35,70,88,120,155]
l = [l[i] for i in range(len(l)) if i not in (0, 4, 5)]
print(l)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = [12,24,35,24,88,120,155]
l = [i for i in l if i != 24]
print(l)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection (common) of the above given lists.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
l3 = list(set(l1) & set(l2))
print(l3) #op [35]
#without using inbuild function
l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l = [12,24,35,24,88,120,155,88,120,155]
l = list(dict.fromkeys(l))

print(l)

#withoutusing inbuild function
l = [12,24,35,24,88,120,155,88,120,155]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Please write a program which count and print the numbers of each character in a string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
s = "hello world"
counter = Counter(s)
for char, count in counter.items():
    print(f"{char}: {count}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Please write a program which accepts a string from console and print the characters that have even indexes.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
s = "H1e2l3l4o5w6o7r8l9d"
s = s[::2]
print(s)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions : Please write a program which prints all permutations of [1,2,3]
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import itertools
print(list(itertools.permutations([1,2,3])))

def permute(nums):
    result = []
    if len(nums) == 1:
        return [nums[:]]
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

nums = [1, 2, 3]
permutations = permute(nums)
for perm in permutations:
    print(perm)