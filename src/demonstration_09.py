
"""
Challenge #9:
Given a string, write a function that returns the "middle" character of the
word.
If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.
Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"

INPUT: input_str --> string
OUTPUT: input_str[middleIndex] --> string
"""

def get_middle(input_str):
  # if the length of the input str is divisble by 2,
  # convert the length of input_str to int and divide by 2 - 1 (incase odd)
  # convert the length of input_str to int and divide by 2 (incase even)
    if (len(input_str) % 2 == 0) :
        middleIndex1 = int(len(input_str) / 2 - 1)
        middleIndex2 = int(len(input_str) / 2)

        return input_str[middleIndex1] + input_str[middleIndex2]
  # convert the length of input_str to int and divide by 2 -.5 (incase decimal)
    else:
        middleIndex = int(len(input_str) / 2 - 0.5)
        return input_str[middleIndex]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))