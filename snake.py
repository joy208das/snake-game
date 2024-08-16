from turtle import Turtle

segment_position = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT =  180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head =  self.segments[0]

    def create_snake(self):
        for position in segment_position:
          self.add_segment(position)
           
    def add_segment(self,position):
           tim = Turtle(shape="square")
           tim.color("white")
           tim.penup()
           tim.goto(position)
           self.segments.append(tim)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())       
                  

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):  # range(start , stop , step)
            new_x = self.segments[n - 1].xcor()
            new_y = self.segments[n - 1].ycor()
            self.segments[n].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
