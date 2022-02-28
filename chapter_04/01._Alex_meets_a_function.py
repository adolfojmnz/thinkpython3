import turtle

def draw(t, sz, angle, speed, lines):
    for i in range(lines):
        t.speed(speed)
        t.forward(sz)
        t.left(angle)

answer = str(input('Do you want to use the default parameters?'
            '\n Write yes or no'))

if answer == 'no':
    ask0 = float(input("Lines' size?"))
    ask1 = float(input("Angle's size?"))
    ask2 = float(input("Turtle's speed"))
    ask3 = int(input("Line to draw?"))
elif answer == 'yes':
    ask0 = 25
    ask1 = 90
    ask2 = 5
    ask3 = 4

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()
draw(alex, ask0, ask1, ask2, ask3)
wn.mainloop()