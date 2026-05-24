#Right-Angled Triangle (Star)
n = 5
for i in range(1, n+1):
    print('*'* i) #Output:
# *
# **
# ***
# ****
# ***** 
print("Right-Angled Triangle (Star)")
# Inverted Right-Angled Triangle (Star)
n =6
for i in range(n, 0 , -1):
    print('*'* i)
print("Inverted Right-Angled Triangle (Star)")

# Pyramid (Star)
n = 6
for i in range(1, n+1):
    print(' '*(n-i)+ '*'*(2*i-1))
print("Pyramid (Star)")
# Daimon(star)
n = 5
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
for i in range(n-1, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))

print("Daimon(star)")

#Right-Angled Triangle with Numbers
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

#Inverted Right-Angled Triangle with Numbers
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

#Pascal's Triangle
n = 5
for i in range(n):
    num = 1
    for j in range(n-i):
        print(' ', end=' ')
    for j in range(i+1):
        print(num, end='   ')
        num = num * (i-j) // (j+1)
    print()

#Right-Angled Triangle with Alphabets
n = 5
for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + j), end=' ')
    print()

#Pyramid with Alphabets
n = 5
for i in range(1, n+1):
    print(' ' * (n-i), end='')
    for j in range(i):
        print(chr(65 + j), end=' ')
    print()
# Floyd's Triangle
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

#Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()