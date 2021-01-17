# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 21
# 321
# 4321

n = int(input())
i = 1
while i <= n:
    j = 1
    k = i
    while j <= i:
        print(k, end="")
        j += 1
        k -= 1
    print()
    i += 1
