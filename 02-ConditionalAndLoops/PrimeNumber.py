n = int(input())
i = 2
flag = False

while i < n:
    if n % i == 0:
        flag = True
    i = i + 1

if flag:
    print("Not Prime")
else:
    print("Prime")
