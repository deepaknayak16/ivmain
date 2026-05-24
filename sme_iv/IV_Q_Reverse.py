'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Programs: Reverse String and 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# $$$$  Method -1 using string slicing 
def reverse_string(s):
    return s[::-1]
#uses 
string_q12 = "Hello World!"
reversed_string = reverse_string(string_q12)
print(f"Orinal string :{string_q12}")
print(f"revised string : {reversed_string}")

# $$$$$  Method -2 Using loop
def reverse_string_2(s):
    reversed_s = ''
    for char in s:
        reversed_s =char + reversed_s
    return reversed_s
#uses 
string_q12_1 = "Python"
reversed_string_2 = reverse_string_2(string_q12_1)
print(f"Original String: {string_q12_1}")
print(f"Reversed String: {reversed_string_2}")
 
## Reverse a String using Recursion
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str("PYTCUMIN")
print(reverse(a))

s = "Deepak"
s = s[::-1]  # Reversing the string using slicing
print(s)

st = "python programming"
result = "".join(st[::-1]) 
print(result)#Output: "gnimmargorp nohtyp"
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Write a Python code to reverse a given list using for loop 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
arr1 = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75] 
reversedList = []
n= len(arr1)
#reverse list using for loop
for i in range(n) :
    reversedList.append(arr1[n - i - 1])
#print lists
print(f'Original List : {arr1}')
print(f'Reversed List : {reversedList}')
############################################################################################
def reverse_list(lst):
    reversed_list = []
    index = 0
    # Find the length of the list manually
    while True:
        try:
            lst[index]  # Try accessing the element at the current index
            index += 1
        except IndexError:
            break  # Stop when index is out of bounds
    # Iterate backward through the list using the length
    while index > 0:
        index -= 1
        reversed_list.append(lst[index])
    return reversed_list
# Test cases
original_list = [1, 2, 3, 4, 5]
reversed_output = reverse_list(original_list)
print("Original List:", original_list)
print("Reversed List:", reversed_output)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Reverse alternative word in a given string  
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def rev_alt(s13):
    word = s13.split()
    for i in range(len(word)):
        if i % 2 == 1:
            word[i] = word[i][::-1]
    return' '.join(word)
s13 = "Deepak nayak software engineer"
result13 = rev_alt(s13)
print(result13) #Output: "Deepak kayan software reenigneer"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Write a Python code to reverse a given string in place
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def rev_word_inplace(s14):
    rev_string = ""
    word = ""
    for char in s14:
        if char == " ":
            rev_string += word[::-1]+" " 
            word = ""
        else:
            word += char
    rev_string+= word[::-1]
    return rev_string
s14 = "you are good nayak"
result14 = rev_word_inplace(s14)
print(result14) #Output: "uoy era doog kayan"
#--------------################## MOethod -2  #### --------------------------------------------------------
def reverse_each_word(s14):
    words = s14.split()  # Split the string into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the reversed words back into a string

# Example usage
s14 = "you are good"
result14_2 = reverse_each_word(s14)
print(result14_2) #Output: "uoy era doog"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: reverse the vowels in each word of given string 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def reverse_consonants_keep_vowels(word):
    vowels = set("aeiouAEIOU")
    chars = list(word)
    consonants = [c for c in chars if c.isalpha() and c not in vowels]
    consonants.reverse()
    result = []
    ci = 0
    for c in chars:
        if c.isalpha() and c not in vowels:
            result.append(consonants[ci])
            ci += 1
        else:
            result.append(c)
    return ''.join(result)

def reverse_vowels_keep_consonants(word):
    vowels = set("aeiouAEIOU")
    chars = list(word)
    vowel_letters = [c for c in chars if c in vowels]
    vowel_letters.reverse()

    result = []
    vi = 0
    for c in chars:
        if c in vowels:
            result.append(vowel_letters[vi])
            vi += 1
        else:
            result.append(c)
    return ''.join(result)

def process_sentence(sentence):
    words = sentence.split()
    rev_consonants = ' '.join(reverse_consonants_keep_vowels(word) for word in words)
    rev_vowels = ' '.join(reverse_vowels_keep_consonants(word) for word in words)
    return rev_consonants, rev_vowels

# Input sentence
s = "Interview with deepak"
out1, out2 = process_sentence(s)

print(out1)  # "Iwvertien hitw keepad"
print(out2)  # "entirveIw with daepek"


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 ::  Write a Python code to reverse a sentence without reversing the words
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def reverse_sentence(sentence):
    reversed_sentence = ' '.join(sentence.split()[::-1])  # Split the sentence into words, reverse the list of words, and join them back into a sentence
    return reversed_sentence

sentence = "I love my India"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)  # Output: "India my love I"
####---------------------------------------------------------------------------------
def reverse_sent(sentence):
    rev_sen = []
    word = ""
    for char in sentence:
        if char != " ":  # If the character is not a space
            word += char # Append the character to the current word
        else:
            rev_sen.append(word) # Add the word to the list
            word = "" # Reset the word
    rev_sen.append(word) # Add the last word
    reversed_sen = "" # Initialize an empty string for the reversed sentence
    for i in range(len(rev_sen) -1, -1, -1): # Iterate backward through the list of words
        reversed_sen += rev_sen[i] + " " # Append the word to the reversed sentence
    return reversed_sen.strip() # Return the reversed sentence
sentence = "I love my India"
result = reverse_sent(sentence)
print("Reversed String:", result) #Output: "India my love I"
####---------------------------------------------------------------------------------
#    words = st2.split()
#    for word in words:
#        rev_s = word + " " + rev_s
#    return rev_s.strip()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: HOW TO reverse a string without affecting special characters
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def reverse_string(string):
    tolist = list(string)
    rightpointer = len(tolist) -1
    leftpointer = 0
    while leftpointer < rightpointer:
        if not tolist[leftpointer].isalpha():
            leftpointer +=1
        elif not tolist[rightpointer].isalpha():
            rightpointer -=1
        else:
            tolist[leftpointer], tolist[rightpointer] = tolist[rightpointer], tolist[leftpointer]
            leftpointer +=1
            rightpointer -=1
    return ''.join(tolist)
string = "l@@me!be*your@@hero%"
print(reverse_string(string))
