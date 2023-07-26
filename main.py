from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake= Snake()
food= Food()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


snake.creating_snake()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()
    #DETECT COLLLISON WITH THE WALL
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
        game_is_on=False
        scoreboard.game_is_over()

    #DETECT COLLISION WITH THE TAIL
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment)< 10:
    #         game_is_on=False
    #         scoreboard.game_is_over()
    seg= snake.segments[1:]
    for segment in seg:
        if snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_is_over()








screen.exitonclick()
