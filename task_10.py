"""
Task 10
Write a program that returns the absolute value of a number retrieved
from the user. The program should keep asking for this number until it is
correctly given.
Remember that the user may not always enter a numeric value, but may
also enter, for example, "cauliflower". Check what happens then and be
sure to handle exceptions.
"""

if __name__ == "__main__":

    try:
        num = float(input("Enter your number: "))
        print(f'Absolute value of a number {num} is {abs(num)}')
    except ValueError:
        print(f'You should enter a number.')
