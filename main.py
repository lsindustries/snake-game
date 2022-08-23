import time
from turtle import Screen
from snake import Snake
from food import Food
from scores import Scores
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("blue")
screen.title("Snake Game 2022")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scores()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()

    #Detecting collision with food
    if snake.segments[0].distance(food) < 10:
        food.new_local()
        snake.extend()
        score.get_point()


    #Detecting collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detecting collision with self
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()