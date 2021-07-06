"""
Challenge #10:
Given a string of space separated integers, write a function that returns the
maximum and minimum integers.
Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"
Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.

INPUT: input_str --> string of numbers
OUTPUT: numbers --> string of numbers
"""

def max_and_min(input_str):
  # map through the int converted string and split the input
    numbers = list(map(int, input_str.split()))
    # return the max and min of the input number string spaced-out
    return ("%d %d" % (max( numbers ), min( numbers )))

print(max_and_min("1 2 3 4 5"))
print(max_and_min("1 2 -3 4 5"))
print(max_and_min("1 9 3 4 -5"))