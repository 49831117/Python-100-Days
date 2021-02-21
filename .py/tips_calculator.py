
print ("Welcome to the tip calculator!\n")

total_bill = float (input ("What was the total bill?\n$"))
tip_percent = int (input ("How much would you like to give? ( 10, 12, or 15 )\n"))
people = int (input ("How many people to split the bill?\n"))

avg_bill = total_bill / people
avg_tip = (total_bill * tip_percent *0.01 ) / people

#round ( float, decimal places)
avg_pay =  round ((avg_bill + avg_tip) , 2)
print ("Each person should pay: $" + "{:.2f}".format(avg_pay) )

# NOTE : https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

# pay = f"{avg_bill + avg_tip}"
# print ( pay )  #但此法只有小數後一位，無法滿足兩位的規格
