MINIMUM_LENGTH = 3


def main():
    password = get_password()

    print('*' * len(password))


def get_password():
    password = input(f"Password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Invalid, password must be at least {MINIMUM_LENGTH} characters. ")
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    return password


main()
