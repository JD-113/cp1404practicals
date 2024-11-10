"""Project management system.
Estimated time: 2 hours
Time taken: 5 hours
"""
from datetime import datetime


class Project:
    """Represents a project with its attributes and methods."""

    def __init__(self, name="", start_date="", priority=0, cost=0.0, completion=0):
        """Initialize a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        return self.priority > other.priority

    def __str__(self):
        """Return string representation of the project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost:.2f}, completion: {self.completion}%"

    def is_complete(self):
        """Determine if project is complete."""
        return self.completion >= 100

    def started_date(self, other):
        if self.start_date > other:
            return True
        else:
            return False
