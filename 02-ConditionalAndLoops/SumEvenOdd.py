# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
# Input format :

# Note : For printing multiple values in one line, put them inside print separated by space.
# You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)

n = int(input())

temp = n
sumEven = 0
sumOdd = 0

while temp > 0:
    lastDigit = temp % 10
    if lastDigit % 2 == 0:
        sumEven = sumEven + lastDigit
    else:
        sumOdd = sumOdd + lastDigit
    temp = temp // 10

print(sumEven, " ", sumOdd)
