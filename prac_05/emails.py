def main():
    email_to_name = {}
    email = input('Email: ')
    while email != '':
        name = extract_name_from_email(email)
        affirmation = input(f"Is your name {name}? (Y/n)")
        if affirmation.upper() != "Y" and affirmation.upper() != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input('Email: ')

    for email, name in email_to_name.items():
        print(name, email)


def extract_name_from_email(email):
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    name = ".".join(name_parts).title()
    return name


main()
