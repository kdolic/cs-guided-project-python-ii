"""
Challenge #7:
Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.
Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"

INPUT: input_str --> string
OUTPUT: myLst --> string
"""
def repeat_it(input_str):
    myLst = []
    s = "-"
  # loop through the length of input str
    for i in range(len(input_str)):
      # uppercase the first new letter in that input str
        myStr = input_str[i].upper()
        # loop through the index of the input str
        for num in range(i):
          # lowercase the other letters that appear & append that string to the list
            myStr += input_str[i].lower()
        myLst.append(myStr)
    # join a '-' between every string input value
    return s.join(myLst)

print(repeat_it("abcd"))
print(repeat_it("RqaEzty"))
print(repeat_it("cwAt"))