import time
from turtle import Screen, Turtle, colormode

screen = Screen()
Y_COR = -280
X_COR = -600

class ColorBox(Turtle):

    def __init__(self):
        super().__init__()
        self.X = -700
        self.Y = 280
        self.X_C = 100
        self.Y_C = 0


    def cordinate(self, color_list):
        for code, color in color_list.items():
            time.sleep(0.1)
            screen.update()
            new_turtle = Turtle()
            new_turtle.penup()
            colormode(255)
            new_turtle.color(color)
            new_turtle.shape("circle")
            new_turtle.shapesize(stretch_wid= 3, stretch_len=3)
            
            if self.X >= 600:
                self.X = -700
                self.Y -= 100 

            new_x = self.X + self.X_C
            new_y = self.Y

            new_turtle.goto(new_x, new_y)

            self.penup()
            self.color("white")
            self.goto(new_x, new_y + -50)
            self.write(color, align="center", font=("courter", 10, "normal"))
            self.X = new_x

        