# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

n = input()

if n == n[::-1]:
    print("true")
else:
    print("false")
