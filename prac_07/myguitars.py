import csv
from prac_07.guitar import Guitar


def main():
    guitars = []
    add_message = []
    name = input("Name: ")

    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        add_message.append([name, year, cost])

        with open("guitars.csv", "a", newline="") as in_file:
            writer = csv.writer(in_file)
            writer.writerows(add_message)
        print(f"{name} ({year}) : {cost} added.\n")

        name = input("Name: ")

    in_file = open('guitars.csv', 'r')

    for line in in_file:
        line = line.strip().split(",")
        guitar = Guitar(line[0], int(line[1]), line[2])
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
