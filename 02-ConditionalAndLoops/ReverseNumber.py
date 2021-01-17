# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

n = int(input())

temp = n
revNo = 0

while temp > 0:
    lastDigit = temp % 10
    temp = temp // 10
    revNo = revNo * 10 + lastDigit

print(revNo)
