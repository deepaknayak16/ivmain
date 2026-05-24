'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Print IP ADDRESS DETAILS IN WINDOWS
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
print(os.system('ipconfig'))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Print IP ADDRESS AND HOST-NAME IN WINDOWS
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Write A Program To IP is pingable or not
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import string
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

# #and then check the response...
# if response == 0:
#   print (hostname, 'is up!')
# else:
#   print (hostname, 'is down!')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os

print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0]) 
config_file_source = r"C:\python_iv_prep\IV_Test"       
parent_path = os.path.dirname(config_file_source)
data_file_source = os.path.join(parent_path, 'Data')
current_path = os.path.abspath(__file__)
utils_path = os.path.join(os.path.dirname(current_path), 'utils')
print("parent_path +++=====", parent_path)
print("current_path  +++=====", current_path)
print("data_file_source  +++=====", data_file_source)
print("utils_path  +++=====",utils_path)
print('path =', pathname)

print('full path =', os.path.abspath("deep.txt")) 
'''
| Function          | Purpose            |
| ----------------- | ------------------ |
| `os.getcwd()`     | Get current folder |
| `os.listdir()`    | List files/folders |
| `os.mkdir()`      | Create directory   |
| `os.remove()`     | Delete file        |
| `os.walk()`       | Traverse folders   |
| `os.path.join()`  | Join paths         |
| `os.path.isdir()` | Check directory    |
| `os.path.isfile()`| Check file         |
'''
import os

print(os.getcwd())      # current directory
print(os.listdir())     # list files/folders

#listdir() with path
folder = "parent"
for item in os.listdir(folder):
    print(item)

#os.path.isdir() → Check if directory
import os
print(os.path.isdir("parent"))

#os.walk() → Traverse all directories/files
import os
for root, dirs, files in os.walk("parent"):
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
#os.path.isfile() to check whether a path is a file.
path = "file1.txt"
if os.path.isfile(path):
    print("It is a file")
else:
    print("Not a file")
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
print(os.system("cd"))

import sys
print(sys.version)
print(sys.version_info)

import os
env_var = os.environ

with open("we.txt", "w") as fl:
    for k, v in env_var.items():
        fl.write(f"{k}:{v}\n")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Write A Program Rename a file in python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#  os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
import os
old_name = "we.txt"
new_name = "wee.txt"

# Renaming the file
#os.rename(old_name, new_name)

if os.path.isfile(new_name):
    print("The file already exists")
else:
    # Rename the file
    os.rename(old_name, new_name)

#  os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Write A Program Remove/Delete a file in python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
relative_path = "wee.txt"
absolute_path = os.path.abspath(relative_path)
print("Q7|| absolute_path +==", absolute_path)
# removing a file with relative path
#os.remove("we.txt")
# remove file with absolute path
#os.remove(r'C:\Users\159625\Documents\Py_Dee\wee.txt')

file_path = absolute_path
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The system cannot find the file specified")


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Copy and move a File in Python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import shutil
current_path1 = os.getcwd()
print("Q8||==", current_path1)
# Define source and destination paths
src_filename = "profit.txt"
dst_filename = "profit.txt"

# Define the source path where the file is currently located
absolute_path_src = os.path.join(current_path1, 'Py_Dee', 'report', src_filename)
print("Q8||== Source path: ", absolute_path_src)

# Define the destination path where the file will be copied/moved
absolute_path_dst = os.path.join(current_path1, 'Py_Dee', 'account', dst_filename)
print("Q8||== Destination path: ", absolute_path_dst)

# Check if the source file exists
if os.path.exists(absolute_path_src):
    # Copy the file from source to destination
    shutil.copy(absolute_path_src, absolute_path_dst)
    print('Q8||== File copied')

    # Now move the file from source to destination
    shutil.move(absolute_path_src, absolute_path_dst)
    print('Q8||== File moved')

else:
    print(f"Q8||== Source file does not exist: {absolute_path_src}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: Copy All Files From A Directory
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import shutil

source_folder = os.path.join(current_path1, 'Py_Dee', 'report')
destination_folder = os.path.join(current_path1, 'Py_Dee', 'account')
if not os.path.exists(source_folder):
    print(f"Source folder does not exist: {source_folder}")
else:
# fetch all files
    for file_name in os.listdir(source_folder):
        # Construct the full file paths
        source = os.path.join(source_folder, file_name)
        destination = os.path.join(destination_folder, file_name)
        
        # Copy only files (skip directories)
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print(f'Q9||== Copied {file_name} to {destination_folder}')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Modular seach path
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#In Python, the module search path is a list of directories that the Python interpreter searches through to find a module 
# when it is imported.
import sys

# Check the current search path
print("Before:", sys.path)

# Add a custom directory
sys.path.append('/path/to/my/modules')

# Check the updated search path
print("After:", sys.path)

# Now you can import modules from that directory
#import my_custom_module


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 11 :: How to execute the system command in python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Method = 1 Using Subprocess.run()
import subprocess

#result_q11 = subprocess.run(['ls', '-l'], capture_output=True, text=True) # Linux filesystem 
result_q11 = subprocess.run(['dir'], shell= True, capture_output= True, text= True) #windows filesystem 

print(result_q11.stdout)

# Method -2  Using subprocess.Popen() for Advanced Control
#stdout=subprocess.DEVNULL to make pip installation quieter
# Execute the command and get the output
process = subprocess.Popen(['ping', '-c', '4', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Capture the output and error
stdout, stderr = process.communicate()

print(stdout.decode())


# Method -3 Using os.system()

os.system('echo "Hellow Deepak"')

#Method -4 s.popen() (Capturing Output)
#os.popen() is similar to os.system() but allows capturing the command's output.

output_q11 = os.popen('dir').read()
print(output_q11)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 11 :: Paramiko 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import paramiko
try:
    # Define connection details
    hostname = 'your.remote.server'
    port = 22
    username = 'your_username'
    password = 'your_password'
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to the server
    ssh.connect(hostname, port, username, password)
    # Execute a command
    stdin, stdout, stderr = ssh.exec_command('ls -l')
    # Print the output
    print("STDOUT:")
    print(stdout.read().decode())

    print("STDERR:")
    print(stderr.read().decode())
    # Open an SFTP session
    sftp = ssh.open_sftp()

    # Upload a file
    local_file_path = 'local_file.txt'
    remote_file_path = 'remote_file.txt'
    sftp.put(local_file_path, remote_file_path)
    print(f"Uploaded {local_file_path} to {remote_file_path}")

    # Download a file
    remote_file_path = 'remote_file.txt'
    local_file_path = 'downloaded_file.txt'
    sftp.get(remote_file_path, local_file_path)
    print(f"Downloaded {remote_file_path} to {local_file_path}")

    # Close the SFTP session and SSH connection
    sftp.close()
except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except paramiko.SSHException as e:
    print(f"SSH error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    if ssh:
        ssh.close()



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Qu
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
