# from turtle import Turtle, Screen

# timmy = Turtle()
# print("print(timmy)", timmy)
# timmy.shape("turtle")
# timmy.color("chocolate4")
# timmy.forward(100)

# my_screen = Screen()
# print("print(my_screen.canvheight)", my_screen.canvheight) # Attribute

# my_screen.exitonclick() # Method

'''
shell system
'''

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("No.", [1, 2, 3], align = 'c')
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], align = 'l')
table.add_column("Type", ["Electric", "Water", "Fire"], align = 'r')

print('table.align\n', table.align)

print(table)








