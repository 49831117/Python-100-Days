Statement
The text is given in a single line. For each word of the text count the number of its occurrences before it.

Example input
one two one two three two four three

Example output
0 0 1 1 0 2 0 1

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/


a = [str(i) for i in input().split()]
list = []

for x in a:
    print(list.count(x), end = " ")
    list += [x]


Model Solution

text = input().split()
times_seen = {}
for word in text:
  if word not in times_seen:
    times_seen[word] = 0
  print(times_seen[word], end=' ')
  times_seen[word] += 1