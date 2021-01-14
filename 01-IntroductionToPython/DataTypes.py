# Dynamically typed
# Not needed to upfront say the interpreter to allocate memory for int, float, char, string etc.
a = 10
print(a)
# python will automatically create some storage and store the address of that variable every, every-time it store any another data_type
a = "avinashbest"
print(a)

# Data Type At a point of instance
x = "Avinash"
print(type(x))
a = 10
print(type(a))

# Address changes when we increment or decrement value
i = 10
print(id(i))
i = i + 1
print(id(i))

# Pointing to the same storage b/w number within this range -5 to 256
a = 10
b = 10
print(id(a))
print(id(b))
