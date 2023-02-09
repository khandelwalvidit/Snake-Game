from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.update()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
    
    # detect collision of snake and food

    if snake.head.distance(food) < 12:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset()
        snake.reset()


    # detect collision with tail

    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 5:
            scoreboard.reset()
            snake.reset()
            


screen.exitonclick()