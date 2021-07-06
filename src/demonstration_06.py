# """
# Challenge #6:

# Return the number (count) of vowels in the given string.

# We will consider `a, e, i, o, u as vowels for this challenge (but not y).

# The input string will only consist of lower case letters and/or spaces.

# INPUT: input_str --> string of vowels
# OUTPUT: count --> integer 
# """

def get_count(input_str):
    count = 0
    # loops through the letters in the input string, if the letter matches the vowels string, increment the count
    for ltr in input_str:
        if ltr in "aeiou":
            count += 1

    return count

print(get_count('aeio u u'))

