li = input().split()
x = int(li[0])
n = int(li[1])

ans = 1
while n > 0:
    ans *= x
    n -= 1

print(ans)
