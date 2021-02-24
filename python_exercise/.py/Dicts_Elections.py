'''
Statement
The first line contains the number of records. After that, each entry contains the name of the candidate and the number of votes they got in some state. Count the results of the elections: sum the number of votes for each candidate. Print candidates in the alphabetical order.

Example input
5
McCain 10
McCain 5
Obama 9
Obama 8
McCain 1

Example output
McCain 16
Obama 17

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/

'''

dict = {}
list1 = []
list2 = []

for i in range(int(input())):
  w1, w2 = input().split()
  if w1 not in list1:
    list1 += [w1]
    list2 += [w2]
  else:
    list2[int(list1.index(w1))] = int(list2[list1.index(w1)])+int(w2)

list3 = sorted(list1)

for k in range(len(list1)):
  q = int(list1.index(list3[k]))
  print(list3[k], list2[q])


# Model Solution

# n = int(input())
# votes_total = {}
# for i in range(n):
#   candidate, num_votes = input().split()
#   if candidate not in votes_total:
#     votes_total[candidate] = 0
#   votes_total[candidate] += int(num_votes)
# for candidate in sorted(votes_total):
#   print(candidate, votes_total[candidate])