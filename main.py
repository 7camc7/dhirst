#import colorgram

#rgb_colors = []
#colors = colorgram.extract('images.jpeg', 30)
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b)
    #rgb_colors.append(new_color)

#print(rgb_colors)

import turtle as t
import random

t.colormode(255) #for random colour
tim = t.Turtle()

color_list = [(245, 235, 47), (201, 10, 32), (220, 161, 81), (240, 230, 3), (39, 212, 63), (41, 79, 178), (27, 38, 163), (236, 41, 144), (207, 72, 18), (17, 149, 20), (188, 15, 10), (211, 28, 127), (73, 9, 27), (214, 139, 195), (235, 155, 4), (99, 173, 211), (59, 14, 10), (12, 96, 61), (87, 208, 150), (19, 19, 44), (97, 234, 195), (83, 80, 214), (238, 158, 210), (216, 80, 56), (239, 169, 157), (10, 225, 237)]

another_line = True

tim.penup()
tim.hideturtle() # once finished
tim.setheading(250)
tim.forward(250)
tim.setheading(0)

dot_count = 0
while another_line:
    for _ in range(10):
        tim.penup()
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        dot_count += 1
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    if dot_count == 100:
        another_line = False



screen = t.Screen()
screen.exitonclick()



