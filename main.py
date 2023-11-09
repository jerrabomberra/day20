# snake game 3 squares - listen up left down right arrows
# possible options are: once move key is detected 
# get position of each part of the snake and each snake part and move the previous one to that one
# each time it eats a bit of food, add another bit to the tail
# if head touches edge then game over (end)
# if snake touches itself then game over (end)

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