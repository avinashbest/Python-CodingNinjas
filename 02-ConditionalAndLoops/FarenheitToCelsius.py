# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.


S = int(input())
E = int(input())
W = int(input())

while S <= E:
    f = S
    c = (f - 32) * 5/9
    f = str(f)
    c = str(int(c))
    print(f  + "\t" + c)
    S = S + W
