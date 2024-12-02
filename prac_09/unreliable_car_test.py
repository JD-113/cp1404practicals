"""CP1404 Prac_09 Unreliable car test"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Testing Unreliable cars """
    great_car = UnreliableCar("Great", 100, 100)
    good_car = UnreliableCar("Good", 100, 60)
    bad_car = UnreliableCar("Bad", 100, 10)

    for i in range(1, 12):
        print(f"Trying to drive the car {i}km:")
        print(f"{great_car.name:12} got {great_car.drive(i):2}km/h")
        print(f"{good_car.name:12} got {good_car.drive(i)}km/h")
        print(f"{bad_car.name:12} got {bad_car.drive(i)}km/h")

    print(great_car)
    print(good_car)
    print(bad_car)


main()
