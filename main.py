from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.bgpic(image)
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    answer_lc = answer_state.lower()

    # Challenge 2
    data = pandas.read_csv("50_states.csv")
    all_states = data["state"].to_list()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_data = data[data.state == answer_state]
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.write(answer_state)


screen.exitonclick()
