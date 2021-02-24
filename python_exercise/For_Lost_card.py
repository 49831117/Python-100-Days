Statement
There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.

Given a number N, followed by N − 1 integers representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

Example input
5
3
5
2
1

Example output
4

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/for_loop_range/  

You may also try step-by-step theory chunks:
https://snakify.org/lessons/for_loop_range/steps/1/


total = 0
sum = 0

a = int (input ()) + 1

for j in range (1, a - 1):
  sum += int (input ())
  
for i in range (1, a):
  total += i

print ( total - sum )



Model Solution

n = int(input())

cards_sum = 0
for i in range(1, n + 1):
  cards_sum += i

for i in range(n - 1):
  cards_sum -= int(input())

print(cards_sum)