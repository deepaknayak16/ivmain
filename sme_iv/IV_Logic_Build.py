# count digit in number
number = 1208345
count = 0
# Handle negative numbers
if number < 0:
    number = -number
# Count digits
while number > 0:
    number = number // 10  # Remove the last digit
    count += 1
print(f"Number of digits: {count}")  #Output = 5


# GCD or HCF
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Replace a with b and b with a % b
    return a

# Example usage
num1 = 56
num2 = 98
print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")

#print all divsior
def divisor(num):
    for i in range(1, num+1):
        if num%i == 0:
            print(i)

divisor(12)

#armstrong: 1**3+5**3+3**3=1+125+27=153
def is_armstrong(num):
    ans = 0
    # Convert the number to a string to easily access digits
    num_str = str(num)
    num_digits = len(num_str)  # Number of digits
    # Calculate the sum of digits raised to the power of num_digits
    for digit in num_str:
        ans += int(digit) ** num_digits
    # Check if the total matches the original number
    return ans == number
# Example usage
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#print name n time
def print_name(name, n):
    if n > 0:
        print(name)
        print_name(name, n - 1)

name = "Pytest"
n = 5
print_name(name, n) # Output: Pytest printed 5 times

name = "Alice"
n = 5
i = 1
while i <= n:  # Loop until i exceeds N
    print(name) # Output: Alice printed 5 times
    i += 1

name = "Alice"
n = 5
count = 0

while count < n:
    print(name)
    count += 1



#hashing
arr = [10, 3, 4, 5, 4, 7, 8, 3, 4, 5, 10]
d = {}
for item in arr:
    d[item] = d.get(item , 0)+1
print (d)
print (d.items())

mxcnt = 0
mxval = -1
mncnt = 100
mnval = None
for key, count in d.items():
    print(key, count)
    if mxcnt < count:
        mxval = key
        mxcnt = count
    if mncnt > count:
        mnval = key
        mncnt = count
print(mxcnt, mxval) #
print(mncnt, mnval)