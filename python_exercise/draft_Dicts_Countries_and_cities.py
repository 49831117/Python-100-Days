Statement
Given a list of countries and cities of each country, then given the names of the cities. For each city print the country in which it is located.

Example input
2
USA Boston Pittsburgh Washington Seattle
UK London Edinburgh Cardiff Belfast
3
Cardiff
Seattle
London

# 5
# A B
# C D E
# F G H I
# J K L M N
# O P Q R S T
# 15
# T
# S
# N
# R
# M
# I
# Q
# L
# H
# E
# P
# K
# G
# D
# B




Example output
UK
USA
UK

# O
# O
# J
# O
# J
# F
# O
# J
# F
# C
# O
# J
# F
# C
# A



Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/




n = int(input())
list = []

for i in range(n):
  list += [str(x) for x in input().split()]

m = int(input())

for j in range(m):
  for k in range(n):
    if input() in list[k]:
      print(list[k][0])


