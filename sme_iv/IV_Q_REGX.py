'''
re.compile('pattern')	#Compile a regular expression pattern provided as a string into a re.Pattern object.
re.search(pattern, str)	#Search for occurrences of the regex pattern inside the target string and return only the first match.
re.match(pattern, str)	#Try to match the regex pattern at the start of the string. It returns a match only if the pattern is located at the beginning of the string.
re.fullmatch(pattern, str)	#Match the regular expression pattern to the entire string from the first to the last character.
re.findall(pattern, str)	#Scans the regex pattern through the entire string and returns all matches.
re.finditer(pattern, str)	#Scans the regex pattern through the entire string and returns an iterator yielding match objects.
re.split(pattern, str)	#It breaks a string into a list of matches as per the given regular expression pattern.
re.sub(pattern, replacement, str)	#Replace one or more occurrences of a pattern in the string with a replacement.
re.subn(pattern, replacement, str)	#Same as re.sub(). The difference is it will return a tuple of two elements.
First, a new string after all replacement, and second the number of replacements it has made
--------------------------------------------------------------------------------------------------------
\A	Matches pattern only at the start of the string.
\Z	Matches pattern only at the end of the string.
\d	Matches to any digit. Short for character classes [0-9].
\D	Matches to any non-digit. short for [^0-9].
\s	Matches any whitespace character. short for character class [ \t\n\x0b\r\f].
\S	Matches any non-whitespace character. Short for [^ \t\n\x0b\r\f].
\w	Matches any alphanumeric character. Short for character class [a-zA-Z_0-9].
\W	Matches any non-alphanumeric character. Short for [^a-zA-Z_0-9]
\b	Matches the empty string, but only at the beginning or end of a word. Matches a word boundary where a word character is [a-zA-Z0-9_].
    For example, '\bJessa\b' matches 'Jessa', 'Jessa.', '(Jessa)', 'Jessa Emma Kelly' but not 'JessaKelly' or 'Jessa5'.
\B	Opposite of a \b. Matches the empty string, but only when it is not at the beginning or end of a word
------------------------------------------------------------------------------------------------------------
*	Match 0 or more repetitions of the preceding regex. For example, a* matches any string that contains zero or more occurrences of 'a'.
+	Match 1 or more repetitions of the preceding regex. For example, a+ matches any string that contains at least one a, i.e., a, aa, aaa, or any number of a's.
?	Match 0 or 1 repetition of the preceding regex. For example, a? matches any string that contains zero or one occurrence of a.
{2}	Matches only 2 copies of the preceding regex. For example, p{3} matches exactly three 'p' characters, but not four.
{2, 4}	Match 2 to 4 repetitions of the preceding regex. For example, a{2,4} matches any string that contains 3 to 5 'a' characters.
{3,}	Matches minimum 3 copies of the preceding regex. It will try to match as many repetitions as possible.
For example, p{3,} matches a minimum of three 'p' characters.
-------------------------------------------------------------------------------------------------------------
*	Match 0 or more repetitions of the preceding regex. For example, a* matches any string that contains zero or more occurrences of 'a'.
+	Match 1 or more repetitions of the preceding regex. For example, a+ matches any string that contains at least one a, i.e., a, aa, aaa, or any number of a's.
?	Match 0 or 1 repetition of the preceding regex. For example, a? matches any string that contains zero or one occurrence of a.
{2}	Matches only 2 copies of the preceding regex. For example, p{3} matches exactly three 'p' characters, but not four.
{2, 4}	Match 2 to 4 repetitions of the preceding regex. For example, a{2,4} matches any string that contains 3 to 5 'a' characters.
{3,}	Matches minimum 3 copies of the preceding regex. It will try to match as many repetitions as possible.
For example, p{3,} matches a minimum of three 'p' characters.
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Remover the Special Charecter from the string 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
intel = "123abcjw:, .@! eiw"
final = re.sub('[^A-Za-z0-9]+', '', intel)
final1 = ''.join(e for e in intel if e.isalnum())
final2 = re.sub(r'\W+','', intel)
print("1st execution", final) #Output: 123abcjweiw
print("2nd execution", final1) #Output: 123abcjweiw
print("3rd execution", final2) #Output: 123abcjweiw

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Romve the Space from the string ex. "ab cd 12 de" o/p "abcd12de"
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
str1 = "ab cd 12 ef"
print (re.sub(r"\s+", "", str1), sep='') #Output: "abcd12ef" Expaination: \s+ matches one or more whitespace characters and replaces them with an empty string, effectively removing all spaces from the input string.
print (re.sub(r"^\s+", "", str1), sep='') #Output: "abcd12ef" Expaination: ^\s+ matches one or more whitespace characters at the beginning of the string and replaces them with an empty string, effectively removing leading spaces from the input string.
print (re.sub(r"\s+$", "", str1), sep='') #Output: "abcd12ef" Expaination: \s+$ matches one or more whitespace characters at the end of the string and replaces them with an empty string, effectively removing trailing spaces from the input string.
print (re.sub(r"^\s+|\s+$", "", str1), sep='') #Output: "abcd12ef" Expaination: ^\s+|\s+$ matches one or more whitespace characters at the beginning (^\s+) or end (\s+$) of the string and replaces them with an empty string, effectively removing both leading and trailing spaces from the input string.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Find all the number O/p[12, 34, 56]
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Input = "ab 12 { cd 34 } ef 563 deepak 3 find 10 job after 2023 "
In_patt2 = r"\d+" #'12', '34', '563', '3', '10', '2023']
In_patt = r"\b\d{2}\b" #['12', '34']
reg_pat = re.compile(In_patt)
reg_pat2 = re.compile(In_patt2)
q_result = reg_pat.findall(Input)
q_result2 = reg_pat2.findall(Input)
print(q_result)
print(q_result2)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Find all the number O/p ['Python', 'pandas']
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
str3= "Jessa loves Python and pandas"
patt3 = r"\w{6}"         #\w matches any alphanumeric character (letters, digits, and underscores). {6} specifies that we want to match exactly 6 of these characters in a row. So, \w{6} will match any sequence of 6 alphanumeric characters.
result3 = re.search(patt3, str3)
print(result3) #<re.Match object; span=(12, 18), match='Python'>
print(result3.group()) #Python
print(re.findall(patt3, str3)) #['Python', 'pandas']

str1 = "Ema Deepak whwrer is a good bad 236"
string_pattern = r"\b\w{3}\b" #\b asserts a word boundary, ensuring that the match is at the start or end of a word. \w{3} matches exactly three alphanumeric characters in a row. \b asserts another word boundary, ensuring that the match is at the end of a word. So, \b\w{3}\b will match any sequence of exactly three alphanumeric characters that are standalone words in the input string.
regex_pattern = re.compile(string_pattern) #
print(type(regex_pattern)) #<class 're.Pattern'>
result = regex_pattern.findall(str1)
print(result) #['Ema', 'bad', '236']

s_result = re.match(r"\w{3}", str1)
print("onlymatch", s_result) #<re.Match object; span=(0, 3), match='Ema'>
print("group match", s_result.group()) #Ema

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Find all IP adresses
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Input string
input_data = """
interface            IP-Address      OK?     Method      Status      Protocol
GigabitEthernet0/0  192.168.1.1     YES     manual      up          up
GigabitEthernet0/1  192.168.2.10    YES     DHCP        up          down
Vlan1               10.0.0.1        YES     manual      down        down
Loopback0           127.0.0.1       YES     manual      up          up
"""
# Regular expression to find IP addresses
ip_addresses = re.findall(r'\d+\.\d+\.\d+\.\d+', input_data) #\d+ matches one or more digits, and \. matches a literal dot. So, \d+\.\d+\.\d+\.\d+ will match any sequence of four groups of digits separated by dots, which is the format of an IPv4 address.
# Output the list of  addresses
print(ip_addresses)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Write a function that checks if a given string is a valid IPv4 address
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
def is_valid_ipv4(input_ip):
    field = input_ip.split(".")   
    if len(field) != 4:
        return False
    for part in field:
        if not part.isdigit():
            return False
        if len(part) > 1 and part.startswith('0'):
            return False  # Leading zero
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True
print(is_valid_ipv4("192.168.0.1"))     # ✅ True
print(is_valid_ipv4("192.168.001.1"))   # ❌ False (leading 0)
print(is_valid_ipv4("256.100.50.25"))   # ❌ False (256 > 255)
print(is_valid_ipv4("192.168.1")) # ❌ False (not 4 octets)
print(is_valid_ipv4("10.0.0.255"))  # ✅ True
print(is_valid_ipv4("256.0.0.1")) # ❌ False (256 > 255)
print(is_valid_ipv4("0.0.0.0")) # ✅ True
print(is_valid_ipv4("01.1.1.1")) # ❌ False (leading 0)

def is_valid_ipv4(ip):
    # Proper regex to match IPv4 structure (4 groups of 1–3 digits)
    match = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
    if match:
        field = ip.split(".")
        for part in field:
            # Reject if not 0 and starts with 0 (leading zero) or out of range
            if (len(part) > 1 and part.startswith('0')) or not (0 <= int(part) <= 255):
                print(f"{ip}","Unacceptable IP address")
                return
        print(f"{ip}","Acceptable IP address")
    else:
        print(f"{ip}","Unacceptable IP address")

is_valid_ipv4("192.168.0.1")  # ✅ True
is_valid_ipv4("192.168.001.1")   # ❌ False (leading 0)
is_valid_ipv4("256.100.50.25")   # ❌ False (256 > 255)
is_valid_ipv4("192.168.1") # ❌ False (not 4 octets)
is_valid_ipv4("10.0.0.255")  # ✅ True
is_valid_ipv4("256.0.0.1") # ❌ False (256 > 255)
is_valid_ipv4("0.0.0.0") # ✅ True
is_valid_ipv4("01.1.1.1") # ❌ False (leading 0)

ip = "10.45.123.1:5004"
# Regex pattern to match IP and port
pattern = r"(\d+)\.(\d+)\.(\d+)\.(\d+):(\d+)"
match = re.match(pattern, ip)
if match:
    oct1, oct2, oct3, oct4, port = match.groups()
    print("Octet 1:", oct1)
    print("Octet 2:", oct2)
    print("Octet 3:", oct3)
    print("Octet 4:", oct4)
    print("Port:", port)
else:
    print("Invalid IP format")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,7}\b'
def check(email):  
    if (re.fullmatch(regex, email)):
        print ("valid Email")
    else:
        print("invalid")
        
if __name__ =='__main__':
    email = "ankitrai326@gmail.com"
    check(email)

email = input("Enter : ")
email = email.strip()
slice_in = email.index("@")
username = email[:slice_in]
domain = email[slice_in + 1:]

print("Username:", username)
print("Domain:", domain)


import re
log = "2009-10-31 02:48:52 is Error Code E9763Q"
# Regex to extract timestamp and error code
match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*Error Code (\w+)", log)
if match:
    timestamp, error_code = match.groups()
    print("Timestamp:", timestamp)
    print("Error Code:", error_code) #Output: Timestamp: 2009-10-31 02:48:52, Error Code: E9763Q
else:
    print("No match found")


'''# Simulate reading from a log file
with open("log.txt", "r") as f:
    data = f.read()
# Regex pattern for timestamp + error code
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*Error Code (\w+)"
# Find all matches
matches = re.findall(pattern, data)
# Display all found entries
for timestamp, code in matches:
    print(f"Timestamp: {timestamp}, Error Code: {code}")'''

# #Generate password using String module

from string import printable
import re
import string 
fc = re.sub(r'\t\n\r\x0b\x0c','', string.printable)
print(fc)
# Python   Split string as vowel found
test_str = "GFGaBst"
res = [s for s in re.split(r'[aieouAEIOU]', test_str) if s]
print(res)

s = "how old 54 are you ?"
age = re.search(r"\d+", s).group()
print(age)