import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"



def main():
    """Main program for guitar processing."""
    print("My Guitars!")
    guitars = get_guitars()

    print("\nThese are my guitars:")
    display_guitars(guitars)

    # Sort guitars by year and display again
    print("\nGuitars sorted by year:")
    guitars.sort()  # Now works due to __lt__ method
    display_guitars(guitars)

def get_guitars():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            line = line.strip().split(",")
            if line:
                name = line[0]
                year = int(line[1])
                cost = float(line[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def main():
    """Main program for guitar processing."""
    print("My Guitars!")
    guitars = get_guitars()

    print("\nThese are my guitars:")
    display_guitars(guitars)

    # Sort guitars by year and display again
    print("\nGuitars sorted by year:")
    guitars.sort()  # Now works due to __lt__ method
    display_guitars(guitars)


if __name__ == '__main__':
    main()
