
#1. Bitwise AND (&)Returns 1 only if both bits are 1.
a = 5      # 0101
b = 3      # 0011
print(a & b)
#2. Bitwise OR (|)Returns 1 if at least one bit is 1.
a = 5      # 0101
b = 3      # 0011
print(a | b)
#3. Bitwise XOR (^)Returns 1 only if the bits are different.
a = 5      # 0101
b = 3      # 0011
print(a ^ b)
#4. Bitwise NOT (~)Inverts the bits (0 becomes 1, and 1 becomes 0).
a = 5      # 0101
print(~a)   # -6 (in two's complement representation)

#Set a Bit
#Set bit at position 2 in num = 5 (101 → 111)
num = 5
pos = 1
num = num | (1 << pos)
print(num)  # 7

#Clear a Bit
#Clear bit at position 2 in num = 7 (111 → 101)
num = 7
pos = 1
num = num & ~(1 << pos)
print(num)  # 5

#Toggle a Bit
#Goal: Flip a bit (0 → 1, 1 → 0)
#Toggle bit at position 1 in num = 5 (101 → 111)
num = 5
pos = 1
num = num ^ (1 << pos)
print(num)  # 7

#Check if a Number is Power of 2
#Key idea: A power of 2 has only one bit set
def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

print(is_power_of_two(8))  # True
print(is_power_of_two(6))  # False
