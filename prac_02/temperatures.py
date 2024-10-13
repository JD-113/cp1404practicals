
MENU = "C = Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"


def main():
    print(MENU)
    choice = input("Enter a choice: ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Your temperature of {celsius:.2f}C is {fahrenheit:.2f}F")
        elif choice == "F":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Your temperature of{fahrenheit:.2f}F is {celsius:.2f}C")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter a choice: ").upper()
    print("Goodbye!")



def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32.0


main()
