"""
CP1404 Prac testing

"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"
    test_car = Car("Test Car")
    assert test_car.fuel == 0, "Car does not set odometer correctly"
    car = Car("Test Car", fuel=10)
    assert car.fuel == 10

def format_phrase(phrase):
    """
    Format a phrase as a sentence.
    >>> format_phrase('hello')
    'Hello.'
    >>> format_phrase('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase('this is a test')
    'This is a test.'
    """

    phrase = phrase.strip()
    phrase = phrase[0].upper() + phrase[1:].lower()
    if not phrase.endswith("."):
        phrase = phrase + "."
    return phrase



run_tests()


doctest.testmod()

