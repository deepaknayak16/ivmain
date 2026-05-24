#Python Arithmetic Operators
'''Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	    Example	
+	      Addition	    x + y	
-	    Subtraction	    x - y	
*	    Multiplication	x * y	
/	    Division	    x / y	
%	    Modulus	        x % y	
**	    Exponentiation	x ** y	
//	    Floor division	x // y  '''

#Python Assignment Operators
'''Assignment operators are used to assign values to variables:

Operator	Example	    Same As	    Try it
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3   #Add and assign
-=	        x -= 3	    x = x - 3	#Subtract and assign
*=	        x *= 3	    x = x * 3	#Multiply and assign
/=	        x /= 3	    x = x / 3	#Divide and assign
%=	        x %= 3	    x = x % 3	#Modulus and assign
**=	        x **= 3	    x = x ** 3	#Exponentiation and assign
//=	        x //= 3	    x = x // 3	#Floor division and assign
&=	        x &= 3	    x = x & 3	#Bitwise AND and assign
|=	        x |= 3	    x = x | 3	#Bitwise OR and assign
^=	        x ^= 3	    x = x ^ 3	#Bitwise XOR and assign
>>=	        x >>= 3	    x = x >> 3	#Right shift and assign
<<=	        x <<= 3	    x = x << 3	#Left shift and assign
:=	        print(x := 3)	    x = 3 # Assignment expression (walrus operator) and assign
                                print(x) '''
#Python Comparison Operators
'''Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	        Equal	x == y	
!=	        Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y '''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: In Python, == and is are both comparison operators, but they serve different purposes:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
== (Equality Operator):
Compares the values of two objects.
Returns True if the values are equal, False otherwise.
'''
#Example:
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) #TRUE

'''
is (Identity Operator):
Checks if two variables refer to the same object in memory.
Returns True if they point to the same object, False otherwise. 
'''
#Example:
x = [1, 2, 3]
y = x
print(x is y) #TURE
z = [1, 2, 3]
print(x is z) #FALSE

# What is an itetator in Python?
''' An iterator is an object that allows you to traverse a container, such as a list or dictionary.
It provides two main methods: __iter__() and __next__().
The __iter__() method returns the iterator object itself.
The __next__() method returns the next element in the container.
When there are no more elements to return, it raises the StopIteration exception.
You can create an iterator using the iter() function.
You can also use a for loop to iterate over an iterator.
'''
#Example:
my_list = [1, 2, 3]
my_iter = iter(my_list)
print(next(my_iter)) #1
print(next(my_iter)) #2
print(next(my_iter)) #3

'''
Feature	                     Iterator	                                                Generator
Implementation	    Requires __iter__() and __next__() methods	                Uses yield to generate values
Memory Usage	    Stores all values in memory	                                Generates values on demand (lazy evaluation)
State Retention	    Does not remember state automatically	                    Remembers state between yield calls
Usage Complexity	More complex	                                            Simpler and concise
Performance	        Can be inefficient for large datasets	                    Highly efficient for large datasets
'''
#Example Generator vs. Iterator for Large Data
# Iterator
class CountUp:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max_num:
            raise StopIteration
        self.current += 1
        return self.current

it = CountUp(1000000)
print(next(it))  # 1
print(next(it))  # 2

# Generator
def count_up(max_num):
    num = 0
    while num < max_num:
        num += 1
        yield num

gen = count_up(1000000)
print(next(gen))  # 1
print(next(gen))  # 2


