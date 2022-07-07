from re import T
import turtle
import math as m

screen = turtle.getscreen()
pen = turtle.Turtle()
text = turtle.Turtle()
text.penup()
text.hideturtle()
pen.hideturtle()
text.setx(-460)
text.sety(-460)


t = 0
a = 0
theta = 0

while True:
    text.undo()
    text.write(f'theta: {theta:>6.2f}\n x: {0.1*t**2*m.cos(t):.2f}\n y: {(0.1)*t**2*m.sin(t):.2f}', align="left")
    pen.goto(0.1*t**2*m.cos(t),(0.1)*t**2*m.sin(t))
    # pen.setheading(theta)
    a += 1
    t = a/(t+1)
    theta = m.atan((t+2*m.tan(t))/(2-t*m.tan(t)))*(180/m.pi)

    print(f'theta:{theta:>6.2f}, a:{a}, t:{t:.2f}')
