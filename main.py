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
screen.tracer()
screen.update()


starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

def snake_start():
    for i in starting_position:
        new_segment = Turtle('square')
        new_segment.speed('fastest')
        new_segment.color('white')
        new_segment.penup()
    
        new_segment.goto(i)
        segments.append(new_segment)
        
snake_start()

print(segments)

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(100)
    break


screen.exitonclick()