"""guitar.py
Guitar class program"""
from datetime import datetime

VINTAGE_AGE = 50

class Guitar:


    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return datetime.now().year - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE