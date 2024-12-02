"""
    read()
    readline()
    readlines()
    for line in file
"""

# 1.
out_file = open("name.txt", 'w')
user_name = input("Enter your name: ")
print(user_name, file=out_file) # why does this have a waring?
out_file.close()

# 2.
infile = open("name.txt", 'r')
user_name = infile.read().strip()
infile.close()
print(f"Hi {user_name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
    print(total)