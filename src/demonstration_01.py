"""
Challenge #1:
Write a function that retrieves the last n elements from a list.
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []
Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

INPUT: a --> array of integer, n --> integer
OUTPUT: lst --> array of numbers after n number in a
"""


def last(a, n):
  # if n input greater than the length of a array, return 'invalid'
    if (n > len(a)):
        return "invalid"
  # list index of a with last number in the length of a
    lst = a[ -n: len(a) ]

    return lst

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))