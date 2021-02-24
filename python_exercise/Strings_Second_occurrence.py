Statement
Given a string that may contain a letter p. Print the index of the second occurrence of p. If the letter p occurs only once, then print -1, and if the string does not contain the letter p, then print -2.

Example input #1
appropriate

Example output #1
2

Example input #2
spare

Example output #2
-1

Example input #3
reason

Example output #3
-2

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/strings_str/  

You may also try step-by-step theory chunks:
https://snakify.org/lessons/strings_str/steps/1/



#s = input ()

# a = s.find ("p")

# if a == -1:
#   print (-2)
# else:
#   print (s.find("p", a+1))



a = input ()

count = 0

if "p" not in a:
  print (-2)
else:
  for i in a:
    if i == "p":
      count += 1

if count == 1:
  print (-1)
elif count > 1:
  s = a.find("p")
  print (a.find("p", s +1))






Model Solution

s = input()
if 'p' in s:
  if s.find('p') == s.rfind('p'):
    print(-1)
  else:
    print(s.find('p') + s[s.find('p') + 1:].find('p') + 1)
else:
  print(-2)