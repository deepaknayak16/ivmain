'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Factorial of a number using recursion
               Using the Iterative technique, calculate factorial in Python.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
def fact(x):
    if x < 0:
        return "No factorial for negative numbers"
    elif x == 0 or x == 1:
        return 1
    return x * fact(x-1)
print(fact(5)) #Output: 120
#-------------------------------
def factorial(n): 
    return n * factorial(n-1) if n > 1 else 1
print(factorial(6)) #Output: 720 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Identify whether the number is Even or Odd
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def e_o(n):
    if n % 2 == 0:
        return n, "even"
    elif n % 3 == 0:
        return n, "Divisible by 3"
    elif n % 2 != 0:
        return n, "odd"
    else:
        return n, "Other"
print(e_o(4))
print(e_o(9))
print(e_o(5))
##----------------------------------------------##
numbers = list(range(1, 11))
output = []
for n in numbers:
    if n % 2 == 0:
        if n % 4 == 0:
            output.append(f"{n} is divisible by 4")
        else:
            output.append(f"{n} is even")
print(output) #o/p ['2 is even', '4 is divisible by 4', '6 is even', '8 is divisible by 4', '10 is even']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Natural Number Sum  #Formula  n * (n + 1) // 2
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def sum_n(n):
    total = 0
    for i in range(0, n + 1): # range(start, stop) 
        total += i
    return total
print(sum_n(6)) #Output: 21
#------------------------------------------------------
natural_number = 5
n = natural_number
for i in range(1, n+1): # range(start, stop)
        print(i) #Output: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Fibonacce series  recursive 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
nterm = 5
if nterm <= 0:
   print("_ve Number")
else:
    result = []
    for i in range(nterm):
        result.append(fibo(i))
    print(result)
    for i in range(nterm):
        print(fibo(i))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Write a function to compute the Fibonacci series up to n. Iterative Fibonacci Series Function:
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fibonacci(0))   # 0
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Prime Number
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def is_prime(number):
   if number <= 1:
      return False  # Numbers <= 1 are not prime  
   for i in range(2, number):
      if number % i == 0:
         return False
   return True
# Test the function
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: Check the string is Palindrom or not ?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# palindrome is a word, number, phrase, or another sequence of characters which read the same backward as forward
def is_pallindrom(string):
   #return string == string [::-1]
   return string.lower() == string[::-1].lower()
print(is_pallindrom('Deepak'))
print(is_pallindrom('rotator'))
#-----------------------------------------------------------------------------
def pall(s):
    org_s = ""  # Initialize an empty string to store the processed characters
    for c in s: # Iterate through each character in the input string
        if c.isalpha(): # Check if the character is an alphabet
            org_s += c.lower()   # Convert to lowercase and append to org_s
    return org_s == org_s[::-1] # Check if the reversed string is equal to the original string
print(pall("ra3ce4 car"))   # True
print(pall("rOtator")) # True
print(pall("Hello"))        # False
print(pall("A man a plan a canal Panama"))  # True

def is_palindrome(arr):
    # Compare the list with its reversed version
    return arr == arr[::-1]
# Example input
arr = [1, 2, 3, 2, 1]
# Check and print result
if is_palindrome(arr):
    print(f"{arr} is a palindrome.")
else:
    print(f"{arr} is not a palindrome.")
#-----------------------------------------------------------------------------
def filter_palindromes(strings):
    return [s for s in strings if pall(s)]
words = ["radar", "python", "level", "world", "ra3ce4 car"]
print(filter_palindromes(words)) # Output: ['radar', 'level', 'ra3ce4 car']
#-----------------------------------------------------------------------------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        # Reverse the number mathematically
        original = x
        reversed_num = 0
        while x != 0:
            reminder = x % 10  # Extract the last digit
            reversed_num = reversed_num * 10 + reminder  # Build the reversed number
            x //= 10  # Remove the last digit
        # A number is a palindrome if it reads the same forward and backward
        return original == reversed_num
# Example usage:
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10)) # Output: False

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Find second heighst number from list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
list7_1 = ["35", "37", "23", "11", "9", "5"]
# Convert the list of strings to integers
list7_1 = [int(num) for num in list7_1]
# Remove duplicates if any and sort the list in descending order
list7_1 = sorted(set(list7_1), reverse=True)
# Get the second highest number
second_highest = list7_1[1] if len(list7_1) > 1 else None
print("Q7|| 1 ==", second_highest)

##################################################################3
list7_2 = [35,37,23,11,9,5]
list7_2_2 = list(set(list7_2)) # to remove duplicate
list7_2_2.sort()
a = list7_2_2[-2]
print("Q7|| 2 ==", a)
#######################################################################
list7_3 =  [34, 32 , 12, 45, 28]
highest = second_highest = float('-inf')  # Set both to negative infinity

for number in list7_3:
   if number > highest:
      second_highest, highest = highest, number  # Update both highest and second_highest
   elif highest > number > second_highest:
      second_highest = number  # Update second_highest only

print("Q7|| 3 ==",second_highest)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: find the largest number in a list.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
numbers = [3, 1, 7, 9, 2, 5]
# Initialize the largest number to the first element
largest = numbers[0]
# Iterate through the list
for num in numbers:
    if num > largest:
        largest = num
print("Q8|| 1 == The largest number is:", largest)
#################################
largest = max(numbers)
print("Q8|| 2 == The largest number is:", largest)
####################################################
largest1 = [10, 20, 4, 45, 99]
print("Q8|| 3 == Largest element is:", largest1[-1:][::-1])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Push or move all the zeor at end of the arrary
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def pushzerotoend(arr):
    pos = 0 #Move zeros to end → fill array from the front → pos = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < n:
        arr[pos] = 0
        pos += 1
    return arr
arr =[1,9,4,0,7,8,0,3,0,4,0,5]
print("Array after pushing all zeros to end of array:", pushzerotoend(arr))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Push or move all the zeor at  of begiening the arrary
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def pushzerotobegin(arr):
    n = len(arr)
    pos = n - 1 # Move zeros to beginning → fill array from the back → pos = n - 1
    for i in range(n - 1, -1, -1): #range(start, stop, step)
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos -= 1
    while pos >= 0:
        arr[pos] = 0
        pos -= 1
    return arr
arr = [1, 2, 0, 4, 0, 5, 0, 7]
print("Array after moving zeros to the beginning:", pushzerotobegin(arr))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: move an array to the left by one step
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
def move_left_by_one(arr):
    n = len(arr)
    if n <= 1:
        return arr  # No need to shift if the array has 0 or 1 element

    first_element = arr[0]  # Store the first element
    for i in range(1, n):
        arr[i - 1] = arr[i]  # Shift each element to the left
    arr[-1] = first_element  # Move the first element to the last position
    return arr
# Example usage
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Array after moving left by one step:", move_left_by_one(arr)) # Output: [2, 3, 4, 5, 1]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: maximum of all subarrays of size k
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
def max_of_subarrays_brute_force(arr, k):
    n = len(arr)
    result = []
    for i in range(n - k + 1):
        result.append(max(arr[i:i + k]))
    return result
# Example usage
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print("Maximum of all subarrays of size", k, ":", max_of_subarrays_brute_force(arr, k))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Find the common elements between two arrays.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Example usage
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [4, 5, 6, 7, 8, 9]
def find_common_elements(arr1, arr2):
    common = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2 and num1 not in common:
                common.append(num1)
    return common
result = find_common_elements(arr1, arr2)
print("Common Elements:", result) # Output: Common Elements: [4, 5, 6]

# Method -1 (List Comperheshion)
list3 = [x for x in arr1 if x in arr2] #if i will addnot in arr2 then it will give me the uncommon element
print("# Method -1 (List Comperheshion Common Elements)",list3) #Output: # Method -1 (List Comperheshion Common Elements) [4, 5, 6]

# Method -2 (SET Function )
set11 = set(arr1)
set22 = set(arr2)
list3 = list(set11 & set22) #If i will use set11 - set22 then it will give me the uncommon element
print("# Method -2 (SET Function Common Elements )", list3) #Output: # Method -2 (SET Function Common Elements ) [4, 5, 6]

#Method -3 (Using Filter Function)
list3 = list(filter(lambda x: x in arr2, arr1)) #if i will use lambda x: x not in arr2 then it will give me the uncommon element
print("#Method -3 (Using Filter Function Common Elements)",list3) #Output: #Method -3 (Using Filter Function Common Elements) [4, 5, 6]

#Method -4(Using Remover Function)
for x in arr2:
  if x  not in arr1: #if i will use if x in arr1 then it will give me the uncommon element
    arr1.remove(x)
print("#Method -4(Using Remover Function Common Elements)", arr1) #  Output: #Method -4(Using Remover Function Common Elements) [4, 5, 6]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Write a Python program to split the list into sublists such that each sublist contains numbers in increasing order
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def split_consecutive(arr):
    result = []
    temp = [arr[0]]  # start with the first element
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:  # check increasing order
            temp.append(arr[i])
        else:
            result.append(temp)  # store the completed group
            temp = [arr[i]]      # start new group
    result.append(temp)          # add the last group
    return result
ip = [10, 11, 12, 2, 5, 8, 3, 7, 1, 3]
op = split_consecutive(ip)
print(op)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: #Find the maximum no. of consecutive one’s in a binary array
                #Ex:  Input :   arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def max_consecutive_ones_with_subarray(arr):
    cnt = 0  # initialize count
    max_count = 0 # initialize max
    start_index = 0
    best_start=0
    best_end =0
    n = len(arr)
    for i in range(n):
        if arr[i] == 1:
            if cnt == 0:
                start_index = i
            cnt += 1
            if cnt > max_count:
                max_count = cnt
                best_start = start_index
                best_end = i
        else:
            cnt = 0
    sub_array = arr[best_start:best_end+1] if max_count > 0 else []
    return max_count, best_start, best_end, sub_array    
arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0] 
max_count, start, end, sub_array = max_consecutive_ones_with_subarray(arr)
print(f"Maximum consecutive 1’s: {max_count}")
print(f"Start index: {start}")
print(f"End index: {end}")
print(f"Subarray of consecutive 1’s: {sub_array}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Find Equilibrium index of an array. Equilibrium index of an array is an index 
such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. 
Ex: Input: arr[] = {-7, 1, 5, 2, -4, 3, 0}
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def all_equilibrium_indices(arr):
    total_sum = sum(arr)
    left_sum = 0
    equilibria = []
    for i, num in enumerate(arr):
        total_sum -= num  # total_sum now represents right_sum
        if left_sum == total_sum:
            lhs = arr[:i]
            rhs = arr[i+1:]
            equilibria.append((i, lhs, rhs, left_sum, total_sum))
        left_sum += num
    return equilibria
# Example
arr = [-7, 1, 5, 2, -4, 3, 0]
equilibria = all_equilibrium_indices(arr)

if equilibria:
    print(f"Total equilibrium indices found: {len(equilibria)}\n")
    for idx, lhs, rhs, lsum, rsum in equilibria:
        print(f"➡️  Equilibrium index: {idx}")
        print(f"   LHS subarray: {lhs}  → sum = {lsum}")
        print(f"   RHS subarray: {rhs}  → sum = {rsum}")
        print("-" * 60)
else:
    print("No equilibrium index found.")
