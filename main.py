# snake game 3 squares - listen up left down right arrows

from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Turtle()
snake.shape("square")
for i in range(3):
    tim.position(0.00,0.00)
screen.exitonclick()