"""CP1404 Prac_09 unreliable car."""

from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven