'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: FIND and COUNT THE LETTER/ "E" IN THE WORD.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
test_str = "GeeksforGeeks"
# using naive method to get count  
# counting e  
count = 0
for i in test_str: 
    if i == 'e': 
        count = count + 1
print (count)

### METHOD -2 USING LAMBDA FUNCTION '''
count1 = sum(map(lambda x : 1 if 'e' in x else 0, test_str)) 
print("Q1||METHOD-2", count1)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: FIND THE NOT REPEATED COUNT THE SENTENCE AND REPEATED THE SENTENCE 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
### METHOD -1  USING LOOP FUNCTION '''
text = "mango mango peach apple 88 a4s apple banana"
words = text.split()
for word in words:
    if text.count(word) == 1:
        print(word)    
    else:
        pass
        # print(f"{word} is repeated {text.count(word)} times")

def word_occurrences(sentence):
    # Convert to lowercase and split into words
    words = sentence.lower().split()

    # Remove punctuation manually (optional)
    cleaned_words = []
    for word in words:
        cleaned_word = ""
        for char in word:
            if char.isalnum():  # Keep only letters and numbers
                cleaned_word += char
        if cleaned_word:
            cleaned_words.append(cleaned_word)
    # Count occurrences manually
    word_count = {}
    for word in cleaned_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
sentence = "mango mango peach apple 88 a4s apple banana"
print(word_occurrences(sentence)) #Output: 
### METHOD -2 USING LAMBDA FUNCTION '''
d = {x:words.count(x)for x in words}
print ("Q-2||METHOD -2", d) #Output: 


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: COUNT THE TOTAL ODD NUMBER IN THE LIST 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
numbers = [3, 2, 5, 7, 4, 9, 6, 9, 5, 8, 3]
### METHOD -1 USING LIST COMPREHESION METHOD '''
odd_nums = [num for num in numbers if num % 2 != 0]
print("Q-3||METHOD -1, odd numbers ", odd_nums )
print(f"Q-3||METHOD -1, odd numbers , {odd_nums}")
print("Q-3||METHOD -1, Total odd numbers ", len(odd_nums) )

### METHOD -2 USING NORMAL FOR LOOP '''
odd_count = 0
for num in numbers:
    if num % 2 != 0:
        odd_count += 1
print("Q-3||METHOD -2, Total odd numbers", odd_count )

### METHOD -3 USING LAMBDA EXPRESSION '''
odd_counts = len(list(filter(lambda x: x % 2 !=0, numbers)))
print(f"Q-3||METHOD -3, Total odd numbers  {odd_count}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: COUNT THE REPATED ELEMENT LIKE THIS (1:3 , 2:2, 3:4) 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
E_List = [1,1,1,1,2,2,2,2,3,3,4,5,5]
Rept_count = {x:E_List.count(x) for x in E_List}
print("Q-4||METHOD -1", Rept_count)

def occrance_lst(mylist5):
    occ ={}
    for item in mylist5:
        if item in occ:
            occ[item] += 1
        else:
            occ[item] = 1
    return occ
print("Q-4|| Method 2", occrance_lst(E_List))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: COUNT THE  ELEMENT WHO REPATED MORE THAN 2 TIMES
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
mylist5 = [1,7,3,7,3,9,3,9,7,9,10,0] 
print ("Q-5||METHOD -1", sorted(set([i for i in mylist5 if mylist5.count(i)>2])))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: COUNT THE NUMBER OF CHARACTER (CHARACTER FREQUENCY) IN A STRING
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
st = "proframing python"
def duplicate(st):
    dct ={}#dictionary
    non_rep ={}#non_repeated
    res=""#result
    lst = [] #list
    for item  in st:
        if item.isalpha():
            if item in dct:
                dct[item] += 1
            else:
                dct[item] =1
    
    for key, value in dct.items():
        if value > 1:
            non_rep[key] = value  #
            lst.append(key) 
            res +=key +(str(value))
    return dct, non_rep, lst, res 
dct, non_rep, lst, res = duplicate(st)

print("Q-6||METHOD -1 ::: string ", res) #Q-6||METHOD -1 ::: string  p2r2o2n2
print("Q-6||METHOD -1 ::: nonrepete ", non_rep) #Q-6||METHOD -1 ::: nonrepete  {'p': 2, 'r': 2, 'o': 2, 'n': 2}
print("Q-6||METHOD -1 ::: in list ", lst) #Q-6||METHOD -1 ::: in list  ['p', 'r', 'o', 'n']
print("Q-6||METHOD -1 ::: Disconari ", dct) #Q-6||METHOD -1 ::: Disconari  {'p': 2, 'r': 2, 'o': 2, 'f': 1, 'a': 1, 'm': 1, 'i': 1, 'n': 2, 'g': 1, 'y': 1, 't': 1, 'h': 1}
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: FIND DUPLICATE ELEMENT IN THE LIST AND COUNT THE ELEMENT in list. 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lst = ['1', '2', '3', '1', 'c', '3', 'c']
def find_duplicate_remove(lst):
    result = {} # Count frequency
    duplicates = []   # Collect duplicates
    for i in lst:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    for key, value in result.items():
        print("{} occurs {} times".format(key, value))
        if value > 1: #if non-duplicate want change operator to ==
            duplicates.append(key)
    return result, duplicates
freq, dup = find_duplicate_remove(lst)
print("Frequency:", freq) #Frequency: {'1': 2, '2': 1, '3': 2, 'c': 2}
print("Duplicates:", dup) #Duplicates: ['1', '3', 'c']
##-----------------------------------------------------------------##
lst = [1, 2, 3, 2, 4, 1, 5]
result = []
for item in lst:
    if item not in result:
        result.append(item)
print(result)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Count repeated characters in a string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
str1 = 'Hello World we@2026#'
dct = {}
result = ""
#result = str1.replace(" ", "").lower()
#or
for ch in str1:
    if ch != " ":
        result += ch.lower()  
for ch in result:
    if ch in dct:
        dct[ch] += 1
    else:
        dct[ch] = 1
for key, value in dct.items(): #iterating through the unordered map
    if value > 1:                #if the count of characters is greater than 1 then duplicate found
        print("Q-8 || METHOD-2:", key, ", count =", value) #Output: 
dct_sort_key = dict(sorted(dct.items()))
print(dct_sort_key) #Output:
dct_sort_value = dict(sorted(dct.items(), key=lambda x: x[1]))
print(dct_sort_value) #Output:

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: Count chars, numbers, symbols in string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
s = "Techm123@#"
chars = nums = symbols = 0
for i in s:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        nums += 1
    else:
        symbols += 1
print("Characters:", chars) #Output: Characters: 5
print("Numbers:", nums)     #Output: Numbers: 3
print("Symbols:", symbols)  #Output: Symbols: 2

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 ::How to count that how many dot character are using in-text string.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
text = 'Hello ............?'
n = 0
dot = [i for i in text if re.match('\.',i) ]
print("Q-10||" "Dot Counting ", len(dot))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions11 :: return true or false if string contains more than one repeated character
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
infi1 = "Deepak"
infi2 = "Kumar"
def has_repeats(s):
    n = len(s)
    duplicates = []
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if s[i] not in duplicates:  # avoid duplicate entries
                    duplicates.append(s[i])
    return len(duplicates) > 0, duplicates
print("Q - 11 ||", has_repeats(infi1))  # True, ['e']
print("Q - 11 ||", has_repeats(infi2))  # False, []
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions12 :: given a string s find the the first non repeating character in it and return its index if it does not exit return -1
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def first_non_repeating_character(s):
    # Create a dictionary to store the frequency of each character
    char_count = {}
    # Count the frequency of each character
    for char in s:
        if char.isalpha():  # Consider only alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    # Find the first character with a frequency of 1
    for index, char in enumerate(s):
        if char.isalpha() and char_count[char] == 1:
            return index
    # If no non-repeating character exists, return -1
    return -1
# Test cases
s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabbcc"

print(first_non_repeating_character(s1))  # Output: 0 (character 'l')
print(first_non_repeating_character(s2))  # Output: 2 (character 'v')
print(first_non_repeating_character(s3))  # Output: -1 (no non-repeating character)
###----------------------------------------------------------------------------------------------------------------
def has_multiple_repeated_characters(s):
    char_count = {}  # Dictionary to store character counts
    repeated_chars = []  # List to store repeated characters

    # Count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Identify characters with more than one occurrence
    for char, count in char_count.items():
        if count > 1:
            repeated_chars.append(char)

    # Check if there are multiple repeated characters
    if len(repeated_chars) > 1:
        print("Repeated characters:", repeated_chars)
        return True
    else:
        return False

# Test cases
print(has_multiple_repeated_characters("sillyspider"))  # Output: True (Repeated characters: ['s', 'i'])
print(has_multiple_repeated_characters("abcd"))         # Output: False
print(has_multiple_repeated_characters("aabbcc"))       # Output: True (Repeated characters: ['a', 'b', 'c'])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions13 :: Print the first non-repeated charcter in agiven string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def first_nonrepeat_char(s13):
    freq ={} #freqency
    for char in s13:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for char in s13:
        if freq[char] == 1:
            return char
    return None
s13 = "sillyspider"
result13 = first_nonrepeat_char(s13)
print("first_nonrepeat_char", result13)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions14 ::  Find the index position of each element of list1 inside list2.
                Map the position of elements from one list to another list based on their values.
                Example list1 = [1, 2, 3, 4, 5, 8] List2 = [8, 4, 5, 2, 1, 3 ]  O/p [4=1, 3=2, 5=3, 1=4, 2=5, 0=8]
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def map_position(list1, list2):
    result = []
    for value in list1:
        result.append(f"{list2.index(value)}={value}")
    return result
list1 = [1, 2, 3, 4, 5, 8]
list2 = [8, 4, 5, 2, 1, 3]
print(map_position(list1, list2))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions15 ::  Remove the duplicate character from the string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def remove_duplicates(s15):
    seen = set()
    result = []
    for char in s15:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
s15 = "sillyspider"
result15 = remove_duplicates(s15)
print("remove_duplicates", result15)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: String Logic ii: Find the Number of Times Each Letter Appeared in the String
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
sentence = "Hi name How are You"

# Convert the sentence to lowercase (optional if you want to count case-insensitive letters)
sentence = sentence.lower()     # Create an empty dictionary to hold the letter counts
letter_count = {}               # Loop through each character in the sentence
for char in sentence:
    if char.isalpha():          # Check if the character is a letter
        if char in letter_count:
            letter_count[char] += 1  # Increment the count if the letter is already in the dictionary
        else:
            letter_count[char] = 1  # Initialize the count if the letter is not in the dictionary

# Print the letter counts
print(letter_count) #output : {'h': 2, 'i': 1, 'n': 1, 'a': 1, 'm': 1, 'e': 2, 'o': 2, 'w': 1, 'r': 1, 'y': 1, 'u': 1}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that returns the number of words in a string.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def word_count(s):
    return len(s.split())
s = "The quick brown fox"
print(word_count(s)) # Output: 4

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that finds the most repeated character in a string.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def most_repeated(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_char = max(char_count, key=char_count.get)
    return max_char, char_count[max_char]
string = "misississippis"
print(most_repeated(string)) 

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that finds the most repeated character in a string.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def separate_and_count(s):
    vowels = ""
    consonants = ""
    digits = ""
    special_char = ""
    spaces = ""
    
    vowel_set = "aeiouAEIOU"
    
    for ch in s:
        if ch in vowel_set:
            vowels += ch
        elif ch.isalpha():
            consonants += ch
        elif ch.isdigit():
            digits += ch
        elif ch.isspace():
            spaces += ch
        else:
            special_char += ch
    
    # Only alphabetic characters
    characters = vowels + consonants
    
    print(f"Input String : {s}\n")
    print("Characters   :", characters)
    print("Vowels       :", vowels, f"({len(vowels)})")
    print("Consonants   :", consonants, f"({len(consonants)})")
    print("Digits       :", digits, f"({len(digits)})")
    print("Spaces       :", repr(spaces), f"({len(spaces)})")
    print("Special Char :", special_char, f"({len(special_char)})")
# Example usage
input_str = "Hello, have DEEpak@23 #!12"
separate_and_count(input_str)
#--------------------------------------------------------------------------
st = "Hello@123#"
def alph_spcl(st):
    al ={}
    sp ={}
    for ch in st:
        if ch.isalpha():
            if ch in al:
                al[ch] += 1
            else:
                al[ch] = 1
        elif not ch.isalnum():
            if ch in sp:
                sp[ch] += 1
            else:
                sp[ch] = 1
    
    for key, value in al.items():
        print("{} occurs {} times".format(key, value))
    for key, value in sp.items():
        print("{} occurs {} times".format(key, value))  
    return al, sp
alph_spcl(st)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that finds the most repeated character in a string.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def countc(a):
    dct = {}
    for items in a:          # Loop through each string in the list
        for item in items:   # Loop through each character in the string
            if item in dct:  # If character already exists in dictionary
                dct[item] += 1
            else:             # Otherwise, add it with count 1
                dct[item] = 1
    return dct

a = ["aaabbccd", "abbccd", "aabbccdd"]
print(countc(a))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function COUNT THE CHARCTER AND CONVERT INTO UPPER TO LOWER AND LOWER TO UPER.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def count_and_swap_case(s):
    freq = {}
    swapped = []
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        swapped.append(ch.lower() if ch.isupper() else ch.upper())
    return freq, "".join(swapped)
s = "HeLLoWoRLd"
freq, swapped = count_and_swap_case(s)
print("Character Count:", freq)
print("Swapped Case String:", swapped)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that finds  all nonrepeting CHARAECTER .
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def nonrepeting():
    s = "aabbdccef"
    freq = {}
    # count frequency of each char
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
   # return all non-repeating
    non_repeating = [ch for ch in s if freq[ch] == 1]
    return non_repeating
print(nonrepeting()) #Output: ['d', 'e', 'f']

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a program to count the number of even and odd numbers in an array of integers.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return even_count, odd_count
arr = [10, 21, 4, 45, 66, 93, 1]
even, odd = count_even_odd(arr)
print(f"Even numbers count: {even}")
print(f"Odd numbers count: {odd}")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 ::  Find the last repeating character in a string
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def last_repeating_char(s):
    seen = set()
    # traverse from right to left
    for ch in reversed(s):
        if ch in seen:
            return ch
        seen.add(ch)
    return None  # if no repeating character
s = "abcae"
s_1 = "adbcresa"
print("Last repeating character:", last_repeating_char(s))
print("Last repeating character:", last_repeating_char(s_1))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Wr
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that finds the most repeated character in a string.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that finds the most repeated character in a string.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 12 :: Write a function that finds the most repeated character in a string.
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''