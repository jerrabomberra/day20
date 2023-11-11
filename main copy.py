from turtle import Turtle, Screen 
import pandas as pd
from snake import Snake
import time

# snake = Snake()
food = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for i in starting_positions:
    new_segment = Turtle('square')
    new_segment.speed(0)
    new_segment.color('white')
    new_segment.penup()    
    new_segment.goto(i)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # for seg_num in range(len(segments)-1, 0 -1):
    #   new_x = segments[seg_num-1].xcor()
    #   new_y = segments[seg_num-1].ycor()
    #   segments[seg_num].goto(new_x, new_y)
    # segments[0].left(90)
    # segments[0].forward(50)
    # break
    


screen.exitonclick()