import random

MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBERS_IN_QUICK_PICK = 6

number_of_picks = int(input("How many quick picks would you like? "))
while number_of_picks < 0:
    print("Only positive numbers try again.")
    number_of_picks = int(input("How many quick picks would you like? "))
for i in range(number_of_picks):
    quick_pick = []
    for j in range(NUMBERS_IN_QUICK_PICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()

    print(" ".join(f"{number:2}" for number in quick_pick))
