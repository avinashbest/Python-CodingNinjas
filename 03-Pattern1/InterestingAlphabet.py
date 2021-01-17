# Print the following pattern for the given number of rows.
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n = int(input())
x = ord('A')
asciiTarget = x + n - 1
targetChar = chr(asciiTarget)
i = 1
while i <= n:
    j = 1
    startChar = chr(ord(targetChar) - i + 1)
    while j <= i:
        charPrinted = chr(ord(startChar) + j - 1)
        print(charPrinted, end="")
        j += 1
    print()
    i += 1
