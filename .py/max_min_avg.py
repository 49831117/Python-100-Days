# stu_height = input ("Input a list of student heights, and seperate by a space.\n").split()
# sum = 0
# num = 0
# for n in range(0, len(stu_height)):
#     # for n in range(x):
#     # range(3) : 0, 1, 2
#     # range ( start, end, step )  #不含 end 值
#     stu_height [n] = int (stu_height[n])
#     sum = sum + stu_height[n]  # sum += stu_height[0]
#     avg = round (sum / len(stu_height))
# print ("Sum of height:", sum )
# print ("Number of height:", len (stu_height))
# print ("Average of height:", avg )

##############

# for height in stu_height:
#     sum += int(height) 
#     num += 1
# avg = round ( sum / num)
# print ("Sum of height:", sum )
# print ("Number of height:", num)
# print ("Average of height:", avg )

##############

stu_scores = input("Input a list of student score, and separate by a space.\n").split()
max = 0
min = 0
for n in stu_scores:
    if int(n) > int(max):
        max = n
    elif int(n) < int(min):
        min = n
print (f"The highest score in the class is {max},and the lowest score is {min}.")
