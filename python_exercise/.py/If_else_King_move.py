'''
Statement
Chess king moves one square in any direction. Given two different squares of the chessboard, determine whether a king can go from the first square to the second one in a single move.

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a king can go from the first square to the second one in a single move or NO otherwise.

https://i.imgur.com/2wNxWMG.png

Example input
4
4
5
5

Example output
YES

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/if_then_else_conditions/ 

You may also try step-by-step theory chunks:
https://snakify.org/lessons/if_then_else_conditions/steps/1/ 

'''

x1 = int (input ())
y1 = int (input ())
x2 = int (input ())
y2 = int (input ())

diff_x = abs (x1 - x2)
diff_y = abs (y1 - y2)
sum = diff_x + diff_y

if diff_x < 2 and diff_y < 2 and sum < 3:
  print ("YES")
else:
  print ("NO")



#  Model Solution

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#   print('YES')
# else:
#   print('NO')