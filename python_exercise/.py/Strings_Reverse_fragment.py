'''
Statement
Given a string in which the letter h occurs at least twice, reverse the sequence of characters enclosed between the first and last occurrences of it.

Example input
In the hole in the ground there lived a hobbit

Example output
In th a devil ereht dnuorg eht ni eloh ehobbit

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/strings_str/   

You may also try step-by-step theory chunks:
https://snakify.org/lessons/strings_str/steps/1/

'''

s = input ()

print ( s[:s.find("h")] + s[s.rfind("h"):s.find("h"):-1] + s[s.rfind("h"):])




#  Model Solution

#  s = input()
# first_pos, last_pos = s.find('h') + 1, s.rfind('h')
# left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
# print(left + middle[::-1] + right)