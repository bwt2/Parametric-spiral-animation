from re import T
import turtle
import tkinter
import math

'''
TODO: Fix arrow on spiral
'''

t = 0
k = 0
theta = 0
n = 1
a = 5

print('''* * * * * * * * * * * * * * *
    Spiral modeled by:
    x = a t^n cos(t)
    y = a t^n sin(t)
    x^2 + y^2 = (at^n)^2
    t in R
* * * * * * * * * * * * * * *''')
while True:
    try:
        n = input('n: ').strip()
        if n == '':
            n = 1
            print(f"Default value chosen (n = {n})")
        else:
            n = int(n)

        while True:
            try:
                a = input('a: ').strip()
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

screen = turtle.getscreen()
screen.clear()
pen = turtle.Turtle()
text = turtle.Turtle()

screen.bgcolor('grey')
turtle.title('Parametric Spiral')
img = tkinter.Image("photo", file="bwspiral.png")
turtle._Screen._root.iconphoto(True, img)

pen.shape('classic')
pen.color('white')
pen.shapesize(0.75,0.75,0.75)

text.color('white')
text.penup()
text.hideturtle()
text.setx(-460)
text.sety(-460)

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

    '''
    DEBUG PRINTS
    print(f'theta:{theta:>6.2f}, k:{k}, t:{t:.2f}')
    '''