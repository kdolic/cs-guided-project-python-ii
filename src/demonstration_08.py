"""
Challenge #8:
Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.
Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"

INPUT: input_int --> integer
OUTPUT: "Even" or "Odd" --> string
"""
def parity(input_int):
  # if the input int is divisble by 2, return "Even", otherwise "Odd"
    if (input_int % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(parity(0))
print(parity(1))
print(parity(2))