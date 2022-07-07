from re import T
import turtle
import math as m

screen = turtle.getscreen()
pen = turtle.Turtle()

t = 0
a = 0
theta = 0

while True:
    pen.goto(0.1*t**2*m.cos(t),(0.1)*t**2*m.sin(t))
    pen.setheading(theta)
    a += 1
    t = a/(t+1)
    theta = m.atan((0.1*(2*t*m.sin(t)+t**2*m.cos(t)))/(0.1*(2*t*m.cos(t)-t**2*m.sin(t))))*(180/m.pi)

    if (90 - theta) < 5:
        theta = -1*theta

    print(f' theta:{theta:>6.2f}, a:{a}, t:{t:.2f},')