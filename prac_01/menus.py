

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

user_name = input("Enter your name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {user_name}")
    elif choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid input")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")