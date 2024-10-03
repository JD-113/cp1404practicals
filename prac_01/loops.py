# A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# # C
number_of_starks = int(input("Enter number of starks: "))
for i in range(number_of_starks):
    print("*", end='')
print()

# D
number_of_starks = int(input("Enter number of starks: "))
for i in range(number_of_starks + 1):
    print("*" * i)
print()