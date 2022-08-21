import time
from turtle import Turtle, Screen
from snake import Snake
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game 2022")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()