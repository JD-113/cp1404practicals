"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A: When the input entered is not valid, can not be converted to an integer e.g.(add,a, s, 32.36.32)
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, but how do you what is changed by if, else? loop? or more exceptions?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
