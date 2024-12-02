from prac_06.guitar import Guitar

def tests():
    name = "Gibson L-5 CES"
    year = 1900
    cost =  16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2000, 1512.9)

    print(f"{guitar.name} get_age() - Expected {124}. Got {guitar.get_age()}")
    print(f"{other_guitar.name} get_age() - Expected {24}. Got {other_guitar.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other_guitar.name} is_vintage() - Expected {False}. Got {other_guitar.is_vintage()}")

tests()