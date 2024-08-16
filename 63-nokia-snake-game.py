from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen  = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("NOKIA Snake GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

end = True
while end:
    screen.update()
    time.sleep(0.09)

    snake.move()
    
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend()
     
    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        end = False
        score.game_over()
     
    for a in snake.segments:
        if a == snake.head:
            pass
        elif snake.head.distance(a) < 10 :
            end = False
            score.game_over()
            
        
            
           

screen.exitonclick()


