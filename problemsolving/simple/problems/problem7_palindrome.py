import math


def palindrome(number):
    rev = 0
    store = None
    n1 = None
    left = None
    n1 = number
    store = number
    while number > 0:
        left = number % 10
        rev = rev * 10 + left
        number = int(number / 10)
    if n1 == rev:
        print("Number %d is Palindrome number", n1)
        pass
    else:
        print("it is not a Palindrome number")
        pass


palindrome(101)
