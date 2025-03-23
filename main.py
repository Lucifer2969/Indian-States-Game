import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
image = "India_states_map.gif"
screen.addshape(image)
turtle.shape(image)

tt = turtle.Turtle()
tt.penup()
tt.hideturtle()

data = pandas.read_csv("indian_states.csv")
state_list = data.states.to_list()
guessed_states = []

game_is_on = True

while game_is_on:
    answer = turtle.textinput(title=f"{len(guessed_states)}/{len(state_list)}Current Score",
                              prompt="What's the state name?:").title()
    if answer in state_list:
        if answer not in guessed_states:
            guessed_states.append(answer)
        current_state = data[data.states == answer]
        tt.goto(current_state.x.item(),current_state.y.item())
        tt.write(arg=answer,align='left', font=('Arial', 8, 'normal'))
    else:
        missed_state_list = []
        for item in state_list:
            if item not in guessed_states:
                missed_state_list.append(item)
        missed_state = pandas.DataFrame(missed_state_list)
        missed_state.to_csv("states_to_learn.csv")
        game_is_on = False

turtle.write(arg=f"{len(guessed_states)}/{len(state_list)}Final Score",align='center', font=('Arial', 20, 'normal'))

turtle.mainloop()
