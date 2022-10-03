from turtle import Turtle, Screen, colormode
from color_box import ColorBox
import colorgram

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1370, height=768)
screen.title("My Python Color Picker")
screen.tracer(0)

t = ColorBox()
t.hideturtle()

rgb_colors = {}
colors = colorgram.extract('tea.jpg', 100)
keys = 1
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors[keys] = new_color
    keys += 1
keys += 1
rgb_colors[keys] = (0, 0, 0)
print(len(rgb_colors))
print(rgb_colors)

t.cordinate(rgb_colors)

screen.mainloop()