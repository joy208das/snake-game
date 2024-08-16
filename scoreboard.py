from turtle import Turtle
Font = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
  
        self.hideturtle()
        self.goto(x=0,y=310)
        self.update_socreboard()
     
    def  update_socreboard(self):
        self.write(f"Score: {self.score}", align= "center", font=Font)
     
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", align ="center" , font =("arial",25,"normal"))    
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_socreboard()    