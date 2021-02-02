
- 大多數情況能輕易完成，但會有少數幾個起始點會有 bug，經思考後得到下列作法。

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def go_on():
    if wall_on_right() == True:
        if front_is_clear() == True:
            move()
    elif right_is_clear() == True:
        turn_right()
        move()
        if right_is_clear() == True:
            turn_right()
            move()
            turn_left()
            if front_is_clear() == True:
                move()

while not at_goal():
    if right_is_clear() == True:
        turn_right()
        move()
        go_on()
    elif front_is_clear() == True:
        go_on()
    else:
        turn_left()
```

