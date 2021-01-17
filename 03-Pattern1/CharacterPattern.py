# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# A
# BC
# CDE
# DEFG


n = int(input())
i = 1
while i <= n:
    j = 1
    startChar = chr(ord('A') + i - 1)
    while j <= i:
        charPrinted = chr(ord(startChar) + j - 1)
        print(charPrinted, end="")
        j += 1
    print()
    i += 1
