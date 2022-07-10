import sys
import turtle
import tkinter
import math
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
t = 1
k = 0
theta = 0
n = 1
a = 5

print('''Spiral modeled by (t in R):
=============================
    x = a t^n cos(t)
    y = a t^n sin(t)
    x^2 + y^2 = (at^n)^2
=============================''')
while True:
    try:
        print('n: ', end='')
        n = input().strip()
        if n == '':
            n = 1
            print(f"Default value chosen (n = {n})")
        else:
            n = int(n)

        while True:
            try:
                print('a: ', end='')
                a = input().strip()
                if a == '':
                    a = 5
                    print(f"Default value chosen (a = {a})")
                else:
                    a = float(a)
                break

            except ValueError:
                print("Invalid Input for a; Enter a number")
                continue
        break

    except ValueError:
        print("Invalid Input for n; Enter an integer")
        continue

print("\nInitializing Animation ...", end ='')

ws = turtle.Screen()
ws.clear()
ws.bgcolor('grey')
turtle.title('Parametric Spiral')
img = tkinter.Image("photo", file=resource_path("bwspiral.png"))
turtle._Screen._root.iconphoto(True, img)

pen = turtle.Turtle()
pen.shape('classic')
pen.color('white')
pen.shapesize(0.75,0.75,0.75)

text = turtle.Turtle()
text.color('white')
text.penup()
text.hideturtle()
text.setx(-460)
text.sety(-460)

pen.penup()
pen.goto((a)*(t**n)*math.cos(t),(a)*(t**n)*math.sin(t))
pen.pendown()

while True:
    text.undo()
    text.write(f'theta: {theta:>6.2f}\n'
               f'x: {(a)*t**n*math.cos(t):>6.2f}\n'
               f'y: {(a)*t**n*math.sin(t):>6.2f}\n'
               f'n: {n:>2.2f}\n'
               f'a: {a:>2.2f}\n'
               f'x = {a} t^{n} cos(t), y = {a} t^{n} sin(t)\n'
               f'x^2 + y^2 = {a**2}t^{2*n}', align="left")

    pen.goto((a)*(t**n)*math.cos(t),(a)*(t**n)*math.sin(t))
    
    pen.setheading(theta)
    
    k += 1
    t = k/(t+1)
    theta = math.atan((t+n*math.tan(t))/(n-t*math.tan(t)))*(180/math.pi)


