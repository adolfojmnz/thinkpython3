import turtle, time

def show_poly():
    try:
        win = turtle.Screen()       # grab/create a resources.
        tess = turtle.Turtle()

        # This dialog could be cancelled,
        # or the convertion to int might fail,
        # or n might be zero.
        n = int(input('How many sides do you want in your polygon?'))
    except:
        raise ValueError(f'{n} is not a legal paramer')
        
        for i in range(n):          # draw the polygon.
            tess.forward(10)
            tess.left(360/n)
        time.sleep(3)               # make program wait a few seconds.
    finally:
        win.bye()                   # close turtle's window.

show_poly()
