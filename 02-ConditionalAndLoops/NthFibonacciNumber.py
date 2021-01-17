# Read input as specified in the question.
# Print output as specified in the question.

# Function for nth Fibonacci number

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program


n = int(input())
print(Fibonacci(n))
