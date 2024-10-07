import random
from turtle import Turtle, Screen

race_on = False
tim = Turtle()
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(width=500, height=400)
colors_str = f"{', '.join(colors)}"
print(colors_str)
screen.title(f"Turtle colors: {colors_str}")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet and user_bet in colors:
    race_on = True
else:
    print("Invalid color entered. Exiting...")
    exit(1)

all_turtles = []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.speed(5)
    y = -100 + i * 40
    tim.goto(-920, y)
    tim.pendown()
    all_turtles.append(tim)

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 900:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            race_on = False
        rand_distance = random.randint(0, 30)
        turtle.forward(rand_distance)

screen.exitonclick()
