from os import stat
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = ".py\\us-states-game\\blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# # 找各州座標的方式
# def get_mouse_click_coor(x,y):
#     print (x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pd.read_csv(".py\\us-states-game\\50_states.csv")
all_states = data.state.to_list()

guess_state = []

while len(guess_state) < 51:
    ans_state = screen.textinput(title = f"({len(guess_state)}/50)Guess the State", prompt = "What's another State's name?").title()

    if ans_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv(".py\\us-states-game\\state_to_learn.csv")
        break
    if ans_state in all_states:
        guess_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        # t.write(ans_state)
        
# state_to_learn.csv


