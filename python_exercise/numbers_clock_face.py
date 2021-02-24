'''
Statement
The hour hand of an analog clock turned α degrees since the midnight. Determine the angle by which the minute hand turned since the start of the current hour. Input and output in this problems are integers.

Example input
190
(6:20)

Example output
120
(20 min)

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/integer_float_numbers/

You may also try step-by-step theory chunks:
https://snakify.org/lessons/integer_float_numbers/steps/1/
'''

hour_angle = int(input())
x = hour_angle*2
minute = x%60
min_angle = minute*6

print (min_angle)


Model
print(int(input()) % 30 * 12)
