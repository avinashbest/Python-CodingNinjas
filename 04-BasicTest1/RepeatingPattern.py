# Print the following pattern for the given number of rows.
# Pattern for N = 3
# 1
# 23
# 4567

n = int(input())
k = 1
i = 1
while i <= n:
    j = 1
    while j <= (2**(i-1)):
        if k == 10:
            k = 1
        print(k, end="")
        k += 1
        j += 1
    print()
    i = i + 1
