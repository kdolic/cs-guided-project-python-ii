"""
Challenge #3:
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20
Notes:
- Bonus: Try to complete this challenge in one line!

INPUT: nums --> string
OUTPUT: product --> integer
"""


def multiply_nums(nums):
  # map through the nums string and separate each value with comma
    numbersLst = map(int, nums.split(', '))
  # set product to 1, loop through each number in the mapped list, multiple each number by product value
    product = 1
    for num in numbersLst:
        product = product * num

    return product

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("10, -2"))