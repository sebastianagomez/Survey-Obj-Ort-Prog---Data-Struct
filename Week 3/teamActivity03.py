"""
03 Team Activity

Instructor: Poulson

Write a class in Python 3 to hold rational numbers (i.e., fractions). Your rational number class should contain an integer for the numerator 
and denominator.

"""

class Rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def prompt(self):
        self.numerator = int(input('Enter the numerator: '))
        self.denominator = int(input('Enter the denominator: '))

    def display(self):
        return print(f'{self.numerator}/{self.denominator}')

    def display_decimal(self):
        return print(self.numerator / self.denominator)

def main():
    number_1 = Rational()
    number_1.display()
    number_1.prompt()
    number_1.display()
    number_1.display_decimal()


if __name__ == "__main__":
    main()