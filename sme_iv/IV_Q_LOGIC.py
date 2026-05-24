# -*- coding: utf-8 -*-
#    return True
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Get Dict keys as form of List
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def getlist(dict):
    list = []
    for keys in dict.keys():
        list.append(keys)
    return(list)
dict = {1:'a', 2:'b', 3:'c'}
print(getlist(dict)) #Output: [1, 2, 3]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Convert a list to multiple intger into a single integer
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
List = [12, 41, 67]
for i in List:
    print(i , end="") #Output: 124167

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: How to itrate- through two list in simontensoly/ Parallaly
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
foo = [1, 2, 3]
bar = ['red', 'while', 'black']
val = [255, 256]
for (f , b, V) in zip(foo, bar, val):
    print ("\n",f,b,V) #Output: 1 red 255, 2 while 256
import itertools
for (f , b, V) in itertools.zip_longest(foo, bar, val):
    print ("\n",f,b,V) #Output: 1 red 255, 2 while 256, 3 black None

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: Multiple Key and multiple value are support in dictnary 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Keys must be immutable types like strings, numbers, or tuples. Mutable types like lists or dictionaries cannot be used as keys. 
# Ex: my_dict = {[1, 2]: "value"}  # This will raise a TypeError because lists are mutable and cannot be used as keys.
#Values can be of any type.
my_dict = {('a', 'b', 'c'): 3,('e', 'f'): 5}
my_dict.update({('e', 'f'): 20})
print(my_dict) # Output: {('a', 'b', 'c'): 3, ('e', 'f'): 20}

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Search a charcter from a string 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def search(char, str):
    n=len(str)
    for i in range(n):
        if str[i] == char:
            return i
    return -1
print("search char", i , search("p", "Python")) #Output: search char 1

# Method 2: Using the built-in find() method ::: index = string.lower().find(char.lower()) # Case-insensitive search

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Print a string on one line using for loop
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
animals = "Elephant"
for animal in animals:
  print(animal, end=' '"\n") #Output: E l e p h a n t (each character on a new line)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: processes numbers in pairs
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums = [9, 4, 7, 6]
s = 0
for i in range(1, len(nums), 2): # Start from index 1 and step by 2 to process pairs (nums[i-1], nums[i])
    s += nums[i-1] - nums[i] # (9-4) + (7-6) = 5 + 1 = 6
print(s) #Output: 6

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: Find all the alphabet from the list
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l_data = [8, 'a', 5, 6, 8, 0, 'e','d']
new_l_data =[]
for c in l_data:
    if str(c).isalpha():         #   if isinstance(ele, str) and ele.isalpha():
        new_l_data += c   #   new_lst.append(ele)
print(new_l_data)
### Methos-2 List Cpmprehesion method 
finalls = [x for x in l_data if isinstance(x, str) and x.isalpha()]
print(finalls)
#Method -3 Lamnda Expression
finalls = list(filter(lambda e: isinstance(e, str) and e.isalpha(), l_data))
print(finalls)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 13 :: Find the missing only one number from the sequence of number from the array
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Using the Sum Formula ---------------------------------------------------
def find_missing_number(arr):
    n = len(arr) + 1  # Include the missing number
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)  # Sum of the numbers in the array
    missing_number = expected_sum - actual_sum  # The missing number is the difference
    return missing_number
# Example Usage
arr = [1, 2, 4, 5, 6] 
missing = find_missing_number(arr)
print("Using the Sum Formula || The missing number is:", missing) 

#Using XOR method --------------------------------------------------------
def find_missing_number_xor(arr):
    n = len(arr) + 1
    xor_full = 0
    xor_array = 0

    for i in range(1, n + 1):
        xor_full ^= i  # XOR of all numbers from 1 to n
    
    for num in arr:
        xor_array ^= num  # XOR of the numbers in the array

    missing_number = xor_full ^ xor_array
    return missing_number

# Example Usage
arr = [1, 2, 4, 5, 6]  # Missing number is 3
missing = find_missing_number_xor(arr)
print("XOR Methos || The missing number is:", missing)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 11 :: Find the missing number from the sequence of letter from the array
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def find_missing_letter(arr):
                                                                        # Convert each letter to its ASCII value
    ascii_values = [ord(char) for char in arr]                          # Find the expected sum of ASCII values from the first to the last character
    expected_sum = sum(range(ascii_values[0], ascii_values[-1] + 1))    # Find the actual sum of the ASCII values of the letters in the array
    actual_sum = sum(ascii_values)                                      # The missing letter's ASCII value is the difference between the expected and actual sums
    missing_letter_ascii = expected_sum - actual_sum                    # Convert the ASCII value back to a character
    return chr(missing_letter_ascii)
# Example Usage
arr = ['a', 'b', 'c', 'e', 'f']  # Missing letter is 'd'
missing_letter = find_missing_letter(arr)
print("The missing letter is:", missing_letter)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 16 ::  
 (Run Length Encoded) conversion
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
inp = 'a2e33'
print(inp) 
alph = [k for k in inp if k.isalpha()]
num = [k for k in (''.join((m,' ')[m.isalpha()] for m in inp)).strip().split(' ')] 
print(*[i*int(j) for i,j in zip(alph,num)],sep='')
##### -------------------------------------RLE Encoding --------------------------------------
def transform_string(s):
    n = len(s)
    result = ""   # Initialize an empty string for the result
    count = 1    # Initialize count for the first character
    for i in range(1, n):
        if s[i] == s[i - 1]:  # If the current character matches the previous one
            count += 1
        else:
            result += s[i - 1] + str(count)  # Append character and its count
            count = 1  # Reset count

    # Add the last character and its count
    result += s[-1] + str(count)
    return result
# Test cases
print(transform_string("abcd"))       # Output: "a1b1c1d1"
print(transform_string("aabbdccdd"))   # Output: "a2b2d1c1d2"
print(transform_string("HiiiYouY"))   # Output: "H1i3Y1o1u1Y1"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 17 ::  Find the unique characters from two strings
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def unique_chars_from_str1(str1, str2):
    result = ""
    for ch in str1:
        if ch not in str2 and ch not in result:
            result += ch

    for ch in str2:
        if ch not in str1 and ch not in result:
            result += ch
    return result
# Example usage
str1 = "apple"
str2 = "grape"
output = unique_chars_from_str1(str1, str2)
print(output) # Output: "lgr"
#--------------------------------------------------------------\
result2 = set(str1) ^ set(str2)
print(result2)# Output: {'l', 'g', 'r'}
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 17 :: Write a function to determine if a string has all unique characters (i.e., no character is repeated).
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def has_all_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True
print(has_all_unique_characters("python"))    # ✅ True
print(has_all_unique_characters("hello"))     # ❌ False (l is repeated)
print(has_all_unique_characters(""))          # ✅ True (empty string)
##------------------------------------------------------
def has_unique_chars(s):
    return len(s) == len(set(s))
string = "abcdef"
strings2= "aabcdef"
print(has_unique_chars(string)) # Output: True
print(has_all_unique_characters(strings2))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 ::  FInd the all pairs of indices that sum up to a target value
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def find_all_pairs(nums, target):
    index_map = {}  # Dictionary to store number and its index
    result = []  # List to store pairs of indices

    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            result.append([index_map[complement], i])  # Store the index pair
        index_map[num] = i  # Store the index of the current number
    
    return result  # Return list of all pairs

# Example usage:
nums = [1, 2, 4, 5, 7, 8]
target = 9
print(find_all_pairs(nums, target))  #OUtput [[2, 3], [1, 4], [0, 5]]


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Group all anagrams from the list
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def group_anagrams(words):
    anagrams = {}  # Dictionary to hold sorted words as keys and lists of anagrams as values
    for word in words:
        sorted_word = ''.join(sorted(word))  # Sort the characters in the word
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []  # Initialize a new list if the key doesn't exist
        anagrams[sorted_word].append(word)  # Append the original word to the list

    return list(anagrams.values())  # Return the grouped anagrams as a list of lists
# Example usage:
words = ["cat", "dog", "tac", "god", "act", "Dormitory", "Dirty room", "listen", "silent"]
print(group_anagrams(words))  # Output: [['cat', 'tac', 'act'], ['dog', 'god'], ['Dormitory', 'Dirty room']]
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase before checking lengths
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)
# Example usage
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("Dormitory", "Dirty room")) # True

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that checks if a string contains all letters of the alphabet atleast once (pangram)
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import string
def contains_all_alphabets(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet
test_string = "The quick brown fox jumps over the lazy dog"
print(contains_all_alphabets(test_string)) # Output: True

from statistics import mean, median, mode, StatisticsError
def compute_statistics(numbers):
    if not numbers:
        return "List is empty."
    try:
        return {
            "mean": mean(numbers),
            "median": median(numbers),
            "mode": mode(numbers)
        }
    except StatisticsError as e:
        mode_val = "No unique mode"
numbers = [1, 2, 2, 3, 4, 5]
print(compute_statistics(numbers)) # Output: {'mean': 2.8333333333333335, 'median': 2.5, 'mode': 2}
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def longest_consecutive_subsequence(nums):
    if not nums:
        return []
    num_set = set(nums)
    longest = []
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            sequence = []
            while current in num_set:
                sequence.append(current)
                current += 1
            if len(sequence) > len(longest):
                longest = sequence
    return longest
# Example
numbers = [9,1, 2, 3, 5, 6, 7, 8, 10]
print(longest_consecutive_subsequence(numbers))  # Output: [5, 6, 7, 8, 9, 10]
nums2 = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_subsequence(nums2)) #Output 
print(longest_consecutive_subsequence(nums2)) #Output: [1, 2, 3, 4]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function to compute the square root of a given non-negative integer n without using built- in square root functions or libraries. Return the floor value of theresult
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def floor_sqrt(n):
    if n < 0:
        return None  # Or raise ValueError("Negative input not allowed")
    if n == 0 or n == 1:
        return n
    start, end  = 1, n
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid       # Store the floor value
            start = mid + 1
        else:
            end = mid - 1
    return result
print(floor_sqrt(10))   # Output: 3
print(floor_sqrt(-25))   # Output: 5
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest substring
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def longsubstring(s):
    n =len(s)
    char_index ={} #
    maxlen = 0 
    left = 0 # Left pointer of start windows
    longest ="" # rember the longest substring 
    for right in range(n):
        char = s[right]
        # If character already seen and inside current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char]= right
        # Update longest substring
        cur_len = right - left +1
        if cur_len > maxlen:
            maxlen = cur_len
            longest = s[left: right+1]
            #if maxlen = 5:
                #break  if O?P abcde
    return longest, maxlen
s="abcdcbcabcdebdcfased"
longsubstr, maxlen =longsubstring(s)
print(f"{longsubstr}, {maxlen}")
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the common longest substring from two string 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def largest_common_substring(s1,s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0]*(n2 +1) for _ in range(n1 +1)]
    max_len, end_index =0, 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] =  dp[i-1][j-1]+1
                if dp[i][j] > max_len:
                    max_len, end_index = dp[i][j], i
            else:
                dp[i][j] = 0
    return s1[end_index - max_len:end_index]
print(largest_common_substring("abcdef", "zcdemf"))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function start checking from the rightmost digit, and the position should count from the rightmost as the highest index.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def check_odd_even_from_right(num):
    num_str = str(num)
    length = len(num_str)
    print(f"Checking number: {num}")

    for idx, digit in enumerate(reversed(num_str)):
        pos_from_right = length - idx - 1  # Rightmost digit = highest index
        is_odd = int(digit) % 2 != 0
        print(f"Digit {digit} at position {pos_from_right} from right → {'Odd' if is_odd else 'Even'}") #Output: Checking number: 34578, Digit 8 at position 4 from right → Even, Digit 7 at position 3 from right → Odd, Digit 5 at position 2 from right → Odd, Digit 4 at position 1 from right → Even, Digit 3 at position 0 from right → Odd

# Example
check_odd_even_from_right(34578)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a program to rotate an array to the right by a given number of steps. 
Example: Input: [1, 2, 3, 4, 5], Rotate by 2 Output: [4, 5, 1, 2, 3]
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle rotations larger than array size
    return arr[-k:] + arr[:-k]
arr = [1, 2, 3, 4, 5]
k = 2
# Rotate and print
rotated = rotate_array(arr, k)
print("Original array:", arr)
print(f"Array rotated right by {k} steps:", rotated) #

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: If a word has more than 5 characters, replace every character in it with #
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def replace_five_char_words(text):
    words = text.split()
    replaced = ['#' * len(word) if len(word) == 5 else word for word in words]
    return ' '.join(replaced)
# Example
input_text = "These words shall be alone eagle trees sky"
output = replace_five_char_words(input_text)
print(output)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that generating all subsequences of a string
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def generate_subsequences(input_string):
    subsequences = []
    n = len(input_string)
    
    # Generate all possible subsequences
    for i in range(1 << n):  # 2^n possible combinations
        subsequence = ""
        for j in range(n):
            if i & (1 << j):  # Check if j-th bit is set
                subsequence += input_string[j]
        if subsequence:  # Exclude empty subsequence
            subsequences.append(subsequence)
    return subsequences
input_string = "abc"
subsequences = generate_subsequences(input_string)
print("Subsequences of", input_string, ":", subsequences) #output: Subsequences of abc : ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 18 :: Write a function that returns the longest consecutive subsequence in a list of numbers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''