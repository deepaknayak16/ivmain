'''
The file object returned by open() has two special methods:
__enter__() → runs when block starts
__exit__() → runs when block ends
f = open("file.txt", "r")
f.__enter__()          # called when entering the block
try:
    data = f.read()
finally:
    f.__exit__()       # called when leaving the block
The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised at some point. 
The file object’s __exit__() method will be called, which will close the file.'''

import os
import re
current_path1 = os.getcwd()
filename_1 = 'ex.txt'
absolute_path_1 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', filename_1)
with open(absolute_path_1, 'r') as text:
    print("read",text.read())
    #text.read()Reads the entire file content from start to end.
    #After this call, the file pointer is at the end of the file (EOF).

    #can reset the file pointer using .seek(0)
    text.seek(0)
    print("readline", text.readline())
    #text.readline()Tries to read one line from the current file position.
    #But since the file pointer is already at EOF (because of read()), it returns an empty string ('').

    #can reset the file pointer using .seek(0)
    text.seek(0)
    print("readlines", text.readlines())
    #text.readlines() Reads all remaining lines into a list.
    #Again, the pointer is still at the end of the file, so it returns an empty list [].

import csv
csv_1 = "data.csv"
absolute_path_csv_1 = os.path.join(current_path1, 'IVQA', 'Py_Dee','data', csv_1)
with open (absolute_path_csv_1,'r') as crfl:
    c_reader = csv.reader(crfl)
    for row in c_reader:
        print(row)

with open (absolute_path_csv_1,'w') as cwfl:
    c_writer = csv.writer(cwfl)
    c_writer.writerow(["Name", "Age"])
    c_writer.writerow(["Deepak", 24])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Find Palindrome from a file
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
current_path1 = os.getcwd()
filename_1 = 'ex.txt'
absolute_path_1 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', filename_1)
with open(absolute_path_1) as text:
    data = text.readlines()
    for line in data:
        line = line.strip()
        line2 = line[::-1]
        if line == line2:
            print ('Palindrome!')
        else:
            print ('Not Palindrome!')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Finds all errors and warnings in a file.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys 
import os 
def find_error_warning(filename_2):
    # Use the filename passed into the function
    error_and_warning = []  # List to store errors and warnings
    i = 0  # Counter for errors
    j = 0  # Counter for warnings
    # Open the file and read its contents
    with open(filename_2, "r") as fp:
        data = fp.readlines()
        
        for line in data:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith("Error:"):
                i += 1  # Increment error counter
                error_and_warning.append((i, "error"))
            
            # Check if the line starts with "WARNING:"
            elif line.startswith("WARNING:"):
                j += 1  # Increment warning counter
                error_and_warning.append((j, line, "warning"))
    
    # Return the list of errors and warnings
    return error_and_warning

# Example usage: pass the correct filename (absolute path or relative path)
filename_2 = absolute_path_1
print("Q2 | OUTPUT find_error_warning ", find_error_warning(filename_2))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Diffence Between write(), writelines(), read(), readline(), readlines()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#The write() method:
#This function inserts the string into the text file on a single line.
#the below line of code will insert the string into the created text file, 
filename_3 = 'read.txt'
absolute_path_2 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', filename_3)

filename_3_1 = absolute_path_2
fp = open(filename_3_1, "w")
fp.write("Hello There \n")
fp.close()

#The writelines() method:
#This function inserts multiple strings at the same time. A list of string elements is created, and each string is then added to the text file.
filename_3_2 = absolute_path_2
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]
fp = open(filename_3_2, "w")
fp.writelines(L)
fp.close()
## The read() method:
#This function returns the bytes read as a string. If no n is specified, it then reads the entire file.
filename_3_3 = absolute_path_2
f = open(filename_3_3, "r")
print("Q3 || Only read", f.read())
## The readline() method:
# This function reads a line from a file and returns it as a string. It reads at most n bytes for the specified n.
# But even if n is greater than the length of the line, it does not read more than one line.
filename_3_4 = absolute_path_2
fp = open(filename_3_4, "r")
print("Q3 || Readline", fp.readline(2))
#The readlines() method:
#This function reads all of the lines and returns them as string elements in a list, one for each line.
filename_3_5 = absolute_path_2
fp1 = open(filename_3_2, "r")
print("Q3 || Last read lines", fp1.readlines())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: how to copy or write coontet of of file1 to file2
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
file1_4 = absolute_path_2
file2_4 = absolute_path_1
with open(file1_4, 'r', encoding='utf-8') as infile, open(file2_4, 'w') as outfile:
    # read sample.txt an and write its content into sample2.txt
    for line in infile:
        outfile.write(line)

# Opening the file to read the contents
f = open(file2_4, "r")
print("Q4 || ",f.read())
f.close()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: Differnece between seek() method and tell()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The seek() function sets the position of a file pointer and the tell() function returns the current position of a file pointer.
'''
f.seek(0)	    Move file pointer to the beginning of a File
f.seek(5)	    Move file pointer five characters ahead from the beginning of a file.
f.seek(0, 2)	Move file pointer to the end of a File
f.seek(5, 1)	Move file pointer five characters ahead from the current position.
f.seek(-5, 1)	Move file pointer five characters behind from the current position.
f.seek(-5, 2)	Move file pointer in the reverse direction. Move it to the 5th character from the end of the file 
'''

with open(absolute_path_1, "r") as fp:
    # Moving the file handle to 6th character 
    fp.seek(6)
    # read file
    print(fp.read())

with open(absolute_path_1, "w+") as fsw:
    fsw.write('My First Line\n')
    fsw.write('My Second Line')
    # move pointer to the beginning
    fsw.seek(0)
    # read file
    print(fsw.read())
with open(absolute_path_1, "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)
    # Inserting new content to the end of the file
    fp.write("\nThis content is added to the end the file")
    # moving to the beginning 
    # again read the whole file
    fp.seek(0)
    print(fp.read())
############################# tell() tel() method ############################
with open(absolute_path_1, "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)

    # getting the file handle position
    print('file handle at:', fp.tell())

    # writing new content
    fp.write("\nDemonstrating tell")

    # getting the file handle position
    print('file handle at:', fp.tell())

    # move to the beginning
    fp.seek(0)
    # getting the file handle position
    print('file handle at:', fp.tell())

    # read entire file
    print('***Printing File Content***')
    print(fp.read())
    print('***Done***')

    # getting the file handle position
    print('file handle at:', fp.tell())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: To combine the contents of two files, sort them in ascending order, and save the result
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Define the file Path
file1_5 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', 'file1_5.txt')
file2_5 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', 'file2_5.txt')
output_file_5 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', 'combine_sort_5.txt')

# Read the contain from both the file 
with open(file1_5, 'r') as f1, open(file2_5, 'r') as f2:
    content1 = f1.read().splitlines()
    content2 = f2.read().splitlines()

# Combine the contents of both files
combined_content = content1 + content2

# Sort the combined content in ascending order
combined_content.sort()

# Write the sorted content to a new file
with open(output_file_5, 'w') as output:
    for item in combined_content:
        output.write(item + '\n')

print(f"Q6 || Combined and sorted content written to {output_file_5}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: How to Search particular string in a file
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def serach_in_file(file_path_7, target_string, case_sensitive=False):
    matched_lines = []
    try:
        with open (file_path_7, 'r', encoding='utf-8') as file_7:
            for line_number, line in enumerate(file_7, start=1):
                source_line= line.strip()
                if case_sensitive:
                    if target_string in source_line:
                        matched_lines.append((line_number, source_line))
                else:
                    if target_string.lower() in source_line.lower():
                        matched_lines.append((line_number, source_line))
    except FileNotFoundError:
        print(f"[Error] File not found: {file_path_7}")
    except PermissionError:
        print(f"[Error] Permission denied: {file_path_7}")
    except Exception as error:
        print(f"[Error] An error occurred: {error}")
    return matched_lines 
# Example usage
current_path = os.getcwd()
file_path_7 = os.path.join(current_path, 'IVQA', 'Py_Dee', 'data', 'ex.txt') 
results = serach_in_file(file_path_7, "Tell", case_sensitive=False)
if results:
    print("Q7 || Found the following matches:")
    for line_number, line in results:
        print(f"Line {line_number}: {line}")
else:
    print("Q7 || No matches found.")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Write a Python program to read numbers from a file, calculate their sum, and print the result.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def cal_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
try:
    file_ivpath1 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', 'numbers.txt')
    with open(file_ivpath1, 'r') as file:
        data = file.read()
    numbers = [int(num) for num in data.split(",")]
    result = cal_sum(numbers)
    print("Sum of numbers:", result)
    print(f"Sum of numbers: {result}")
except Exception as e:
    print("An error occurred:", str(e))
    print(f"An error occurred: {e}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Write a Python program to read a properties file and print the key-value pairs.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def read_properties(filepath):
    properties = {}
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties
# Example usage
if __name__ == "__main__":
    file_path_8 = os.path.join(current_path1, 'IVQA', 'Py_Dee', 'data', 'config.properties')
    props = read_properties(file_path_8)

# Print all key-value pairs
for key, value in props.items():
    print(f"{key} = {value}")

# Access specific values
print("\nUsername:", props.get("username"))
print("Server:", props.get("server"))


from pathlib import Path
fpath = Path('Download/deep.txt').absolute()
print(fpath)
if fpath.exists():
    print("✅ File exists:", fpath)
else:
    print("❌ File not found:", fpath)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Write a Python program to read a properties file and print the key-value pairs.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
##Print the 1st 6 line from a file 
n = 4
with open(absolute_path_1, 'r') as my_file:
    head = [next(my_file) for x in range(n)]
print("1st 4 lines ******")
print(head)

'''--------------------------------------------------------------------------------
parent/
│
├── child1/
│   ├── file1.txt
│   └── file2.txt
│
└── child2/
    ├── file3.txt
    └── file4.txt
-------------------------------------------------------------------------------
Question: Write a Python program to read all files in the parent directory and print their contents.
''' 
import os
parent_dir = "parent"
for root, dirs, files in os.walk(parent_dir):
    for file in files:
        file_path = os.path.join(root, file)

        print(f"\nReading: {file_path}")

        with open(file_path, "r") as f:
            content = f.read()

            print(content)


