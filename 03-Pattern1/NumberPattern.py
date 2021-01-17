# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1234
# 123
# 12
# 1

n = int(input())
i = 0
while i <= n:
    j = 1
    temp = 1
    while j <= n - i:
        print(temp, end='')
        j = j + 1
        temp = temp + 1
    print()
    i = i + 1
