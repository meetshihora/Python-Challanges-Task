# Task 4: I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

# Solution:

s = "maine 200 banana khaye"
s = s.replace("200", "10")
s = s.replace("banana", "samosa")
print(s)

# Output: 'maine 10 samosa khaye'