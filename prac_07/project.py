"""Project management system.
Estimated time: 2 hours
"""
from datetime import datetime


class Project:
    """Represents a project with its attributes and methods."""

    def __init__(self, name="", start_date="", priority=0, cost=0.0, completion=0):
        """Initialize a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = float(cost)
        self.completion = completion

    def __str__(self):
        """Return string representation of the project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        """Enable sorting projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is complete."""
        return self.completion == 100