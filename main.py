import time
import random
from turtle import Turtle, Screen
from rich import print
from rich.panel import Panel

from libs.screenSize import screenSize


colors = ["red", "cyan", "yellow", "green", "blue", "purple"]
colors_str = f"{', '.join(colors)}"
print(f"Turtle colors: {colors_str}")
user_bet = input("Which turtle will win the race? Enter a color: ")

race_on = False
tim = Turtle()
screen = Screen()
screens = screenSize()
if len(screens) > 1:
    screen_width = screens[0].width + screens[1].width
else:
    screen_width = screens[0].width

screen_total_width = screen_width - 60
screen.setup(width=screen_total_width, height=400, startx=20, starty=200)
screen.title(f"Turtle colors: {colors_str}")
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
    start_x = -(screen_total_width / 2) + 20
    tim.goto(start_x, y)
    all_turtles.append(tim)

message = "";
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > (screen_width/2) - 20:
            winning_color = turtle.pencolor()
            if winning_color != user_bet:
                message = f"[red]You've lost! The {winning_color} turtle is the winner!";
            else:
                message = f"[green]You've won! The {winning_color} turtle is the winner!";
            race_on = False
            time.sleep(1)
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

screen.bye()
print(Panel(message))
