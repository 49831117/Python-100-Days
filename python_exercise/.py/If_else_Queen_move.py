'''
Statement
Chess queen moves horizontally, vertically or diagonally in any number of squares. Given two different squares of the chessboard, determine whether a queen can go from the first square to the second one in a single move. 

The program receives four numbers from 1 to 8 each specifying the column and the row number, first two - for the first square, and the last two - for the second square. The program should output YES if a queen can go from the first square to the second one in a single move or NO otherwise.


https://i.imgur.com/D4O2iuo.png

Example input
1
1
2
2

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

if diff_x == diff_y:
  print ("YES")
elif diff_y == 0 or diff_x == 0:
  print ("YES")
else:
  print ("NO")



# Model Solution

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
#   print('YES')
# else:
#   print('NO')