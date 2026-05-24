a = "Monty Python"
word = ''
for letter in a:
    word += letter
    print(word)

dw={}
dw['read'] = 0
dw['write'] = 0

f = [ '1, read, 15',
 '2, write, 10',
 '3, read, 10',
 '4, write, 13']
for lines in f:
    print(lines)
    line = lines.split(', ')
    dw[line[1]] += int(line[-1])
print(dw)

##Read Specific Lines 2nd and 5th From a File in Python
import os
#data = os.startfile('')
with open(r"C:/Users/159625/Documents/Py_Dee/ex.txt", "r") as myfile:
    line_numbers = [2, 5]
    # To store lines
    lines = []
    for i, line in enumerate(myfile):
        # read line 4 and 7
        if i in line_numbers:
            lines.append(line.strip())
        elif i > 5:
            # don't read after line 7 to save time
            break
print("********???? line", lines)


def countCharacterType(str): 
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0
    spaces = 0

    for i in range(0, len(str)):  
          
        ch = str[i]  
  
        if ( (ch >= 'a' and ch <= 'z') or 
             (ch >= 'A' and ch <= 'Z') ):

            ch = ch.lower() 
  
            if (ch == 'a' or ch == 'e' or ch == 'i' 
                        or ch == 'o' or ch == 'u'): 
                vowels += 1
            else: 
                consonant += 1
          
        elif (ch >= '0' and ch <= '9'): 
            digit += 1
        elif (str[i] ==' '):
            spaces = spaces + 1    
        else: 
            specialChar += 1
      
    print("Vowels:", vowels) 
    print("Consonant:", consonant)  
    print("Digit:", digit)
    print("White spaces:", spaces)  
    print("Special Character:", specialChar)  
str = "DEEpak@23 12"
countCharacterType(str)


# a = ['a','e','i','o','u','A','E','I','O','U',' ']
# b = "Hello, have a good day"
# for i in b:
#   if i not in a:
#     b = b[:b.index(i)]+b[b.index(i)+1:]
# print (b)

# #Can you write an efficient code to count the number of capital letters in a file?
SOME_LARGE_FILE =r"C:/Users/159625/Documents/Py_Dee/ex.txt"
with open(SOME_LARGE_FILE) as countletter:
    count = 0
    text = countletter.read()
    for character in text:
        if character.isupper():
            count += 1
print("capital letters::::::::::::::", count)

list = ["2", "5", "7", "8", "1"]
list = [int(i) for i in list]
list.sort()
print ("hhhhh", list)

def countOccurences(str, word): 
      
    a = str.split(" ")  
    count = 0
    for i in range(0, len(a)):   
        if (word == a[i]): 
           count = count + 1     
    return count
str ="GeeksforGeeks A computer dee science portal dee for geeks  "
word ="dee"
print(countOccurences(str, word)) 

class Node: 
      
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
          
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.counter = 0
          
    # Counts the no . of occurances of a node 
    # (seach_for) in a linkded list (head) 
    def count(self, li, key):      
        
        # Base case  
        if(not li):  
            return self.counter 
          
        # If key is present in  
        # current node, return true  
        if(li.data == key):  
            self.counter = self.counter + 1
          
        # Recur for remaining list  
        return self.count(li.next, key)  
  
    # Function to insert a new node  
    # at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the  
    # linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
  
# Driver Code 
llist = LinkedList() 
llist.push(1) 
llist.push(3)
llist.push(8)
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1) 
  
# Check for the count function 
#b = input()
#print(b) 
print ("count of", 3 , llist.count(llist.head, 3)) 

import random
number_even = (random.randint(0,100)) * 2
number_odd = (random.randint(0,100)) * 2 +1
print("number_even", number_even)
print("number_odd", number_odd)
##Romoval of togethered element from list

# from itertools import groupby
# h = [1,1,1,1,1,1,2,3,4,4,5,1,2]
# nl = [k for k, g in groupby(h) if len(list(g)) < 2]
# print("Romoval of togethered element from list", nl)





#Python isinstance() function returns True if the object is of specified types, and if it does not match then returns False