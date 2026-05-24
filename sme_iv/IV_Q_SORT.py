"""sort():
This is a method that operates on lists directly, modifying the original list in place. It doesn't return a new list.
sorted():
This is a built-in function that takes any iterable as an argument and returns a new sorted list, leaving the original iterable unchanged.
2. Usage:
sort().
Python


   my_list = [3, 1, 4, 2]
   my_list.sort()
   print(my_list)  # Output: [1, 2, 3, 4] 
sorted().
Python


   my_list = [3, 1, 4, 2]
   new_list = sorted(my_list)
   print(new_list)  # Output: [1, 2, 3, 4]
   print(my_list)  # Output: [3, 1, 4, 2]  (Original list unchanged)
3. Data Types:
sort(): Only works on lists.
sorted(): Works on any iterable, including lists, tuples, strings, and dictionaries.
4. Return Value:
sort(): Returns None.
sorted(): Returns a new sorted list.
"""

## Sort the list 
from operator import le
from sys import last_exc


L1 = ["9", "1", "5", "2", "0", "3"]
L1.sort()
print("Ouve", L1)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Sorting a list/array odd numbers first, then even numbers in Python
L = [5,6,4,7,11,14,12,1,3]

l_even = sorted(L, key = lambda x:(x%2, x))
print(l_even)

## odd numbers followed by even numbers , each in ascending order
l_o_e_a = sorted(L, key = lambda x:(not x%2, x))
print(l_o_e_a)

## even numbers followed by odd numbers , each in descending order
l_e_o_d = sorted(L, key = lambda x:(not x%2, x), reverse=True)
print(l_e_o_d)
## odd numbers followed by even numbers , each in descending order
l_o_e_d = sorted(L, key = lambda x:(x%2, x), reverse=True)
print(l_o_e_d)

###### OTHRT WAY TO SOLVE ############################################ 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: move all the odd number to the front and even numbers to the end in an array
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def rearrange_arr(arr):
   odd_num = [x for x in arr if x%2 != 0]
   even_num =[x for x in arr if x%2 == 0]
   return sorted(odd_num) + sorted (even_num)
arr = [8,3,5,2,1,4,7,6]
result = rearrange_arr(arr)
print(arr)
print(result)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#How to sort mixed data type.
str_num =[5, "1", 100, 2.3,"34"]
s1 = [i for i in str_num if isinstance(i,int) or isinstance(i,float)]
s2 = [j for j in str_num if isinstance(j,str)]
str_num = sorted(s1) + sorted(s2)
print (str_num)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

## Sort the list without using any inbuilt method 
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print( "Sort the list without using any inbuilt method" , new_list)
##### OTHER WAY Around ############
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
for i in range(len(my_list) - 1):
  for j in range(i + 1, len(my_list)):
    if my_list[i] > my_list[j]:
      my_list[i], my_list[j] = my_list[j], my_list[i]

print(" OTHER WAY Around", my_list)


# Python Program
# Sorted vs sort

li = (3, 1, 2, 4)
print("using Sorted function :", sorted(li))
print("Tuple remains same :", li)

# sort using sort method
li_list = list(li)  # Convert tuple to a list
li_list.sort()  # Sort the list in place
print("List is changed and sorted:", li_list)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Function to perform bubble sort on a list
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #return arr #for sorted list
def merge_sorted_lists(list1, list2):
    sorted_list = []
    i = j = 0  
    # Merge lists by comparing elements
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    # Append any remaining elements from list1
    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1
    # Append any remaining elements from list2
    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1
    return sorted_list
# Example lists
list1 = [4, 7, 3, 2, 5]
list2 = [6, 1, 9, 5, 8, 2]
# Sort the individual lists
bubble_sort(list1)
bubble_sort(list2)
# Merge the sorted lists
r_sorted_list = merge_sorted_lists(list1, list2)

print("Sorted List:", r_sorted_list)

# result = []
# for i in r_sorted_list:
#     if i not in result:
#             result.append(i)
#print (result)



lst = [[1, 0], [1, 3], [1, 4], [2, 0]]
lst.sort(key = lambda x:x[1])
print(lst)

#It finds its index in the sorted array by comparing the original array with the sorted array and returns the indices of the original elements in the sorted order.
arr = [5, 1, 6, 3, 7]
def sort(arr):
    temp = arr.copy()
    n = len(temp)
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    return temp

sorted_arr = sort(arr)
print("Sorted:", sorted_arr)  #Sorted: [1, 3, 5, 6, 7]
# Now use the original `arr` for comparison
result = [sorted_arr.index(num) for num in arr]
print("Result:", result)  #Result: [2, 0, 3, 1, 4]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Sort the words by last character and first character
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sort the words by last character
def sort_by_last_frist_char(words):
    last_char = sorted(words, key=lambda x: x[-1])
    first_char = sorted(words, key=lambda x: x[0])
    last_char_desc = sorted(words, key=lambda x: x[-1], reverse=True)
    first_char_desc = sorted(words, key=lambda x: x[0], reverse=True)
    return last_char , first_char, last_char_desc, first_char_desc 
# Example usage
words = ["banana", "apple", "cherry", "date"]
last_char, first_char, last_char_desc, first_char_desc = sort_by_last_frist_char(words)
print("Sorted words by last character:", last_char) # Output: ["banana", "apple", "date", "cherry"]
print("Sorted words by first character:", first_char) # Output: ["apple", "banana", "cherry", "date"]
print("Sorted words by last character (descending):", last_char_desc) # Output: ["cherry", "date", "apple", "banana"]
print("Sorted words by first character (descending):", first_char_desc) # Output: ["date", "cherry", "banana", "apple"]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Sort the words by length
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sort the words by length
def sort_by_length(words):
    return sorted(words, key=len)
# Example usage
words = ["banana", "apple", "cherry", "date"]
sorted_words = sort_by_length(words)
print("Sorted words by length:", sorted_words)

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
n = len(days)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(days[j]) > len(days[j + 1]):
            days[j], days[j + 1] = days[j + 1], days[j]
print(days) #['monday', 'sunday', 'friday', 'tuesday', 'thursday', 'saturday', 'wednesday']
#--------------------------------------------------------------------------------------------------
re = [sto for sto in sorted(days, key =len)]
print(re)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Reorder elements based on indices
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#@creating a new list and placing elements at their respective positions based on the indices list
data = [10, 20, 30, 40]
indices = [2, 1, 0, 3]
n = len(data)
# Creating a new list of size n
output = [0] * n
# Placing elements in their respective positions
for i in range(n):
    output[indices[i]] = data[i]
print(output) #[30, 20, 10, 40]
