import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
states_dic = states_data.to_dict("records")

correct_ans = []
correct = 0

while len(correct_ans) < 50:
    state = screen.textinput(title=f"{correct}/50 States Correct", prompt="Whats another state name?").lower()

    if state == "exit":
        learn_state = []

        for st in states_dic:
            if st["state"] not in correct_ans:
                learn_state.append(st["state"])
        csv_list = pd.DataFrame(learn_state)
        csv_list.to_csv("states_to_be_learn.csv")

        break

    for st in states_dic:
        if st["state"].lower() == state:
            correct_ans.append(st["state"])
            correct += 1
            state_name = turtle.Turtle()
            state_name.speed(0)
            state_name.hideturtle()
            state_name.penup()
            state_name.goto(st["x"], st["y"])
            state_name.write(f"{st["state"]}", align="center", font=("Courier", 8, "bold"))
