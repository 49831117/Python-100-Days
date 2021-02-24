Statement
Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.

Example input
2
apple orange banana
banana orange

# 3
# iawkvxlhqwjm rwcahhaesy kbfahrmup huq w rzllq pq ufszcjb
# wmjdbhcwhxzlhlf
# jeeyfhbsauapwnpmskgh rzllq rzllq wmjdbhcwhxzlhlf rzllq rzllq jeeyfhbsauapwnpmskgh wmjdbhcwhxzlhlf rzllq jeeyfhbsauapwnpmskgh jeeyfhbsauapwnpmskgh


Example output
banana

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/


line = int(input())
list0 = []

for i in range(line):
  list0 += [input().split()]
print(list0)

p = set(list0.split("], ["))
# list_name = sorted(list(p))
# list_num = []

# for i in list_name:
#   list_num += [list.count(i)]
# max = int(max(list_num))
# print(list_name[max])


