# -------------------------------------------------------------------------------
# Name:        Python Lessons
# Purpose:     Educational
# Chapter:     3. Hello, little turtles!
# Author:      Adolfo Jiménez
#
# Started:     15/04/2020
# Finished:    26/05/2020
# Copyright:   (c) Adolfo Jiménez 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
quit_program = False
while True or quit_program == True:
    n = int(input('Please enter a number from 1-9 to run a program.'
                  '\n Enter 0 to exit.'
                  '\n 0: Exit.'
                  '\n 1: Hello, Alex!'
                  '\n 2: Hello, Tess!'
                  '\n 3: Tessa and Alex'
                  '\n 4: Party invitation'
                  '\n 5: Alex\'s box N°1'
                  '\n 6: Alex\'s box N°2'
                  '\n 7: Tessa shape'
                  '\n 8: Proposed exercises'
                  '\n 9: Seconds countdown'
                  '\n I: '))
    if n == 0:
        break

    if n == 1:
        import turtle

        wn = turtle.Screen()
        wn.title("Hello, Alex!")
        alex = turtle.Turtle()
        alex.forward(80)
        alex.left(90)
        alex.forward(40)
        alex.left(90)
        alex.forward(80)
        alex.left(90)
        alex.forward(40)
        wn.mainloop()
    pass
    if n == 2:
        import turtle

        wn = turtle.Screen()
        wn.bgcolor(str(input("Please, define the windows' blackgroud color\n>")))

        wn.title("Hello, Tess!")

        tess = turtle.Turtle()
        tess.color(str(input("Please, define the pen's color\n> ")))
        tess.pensize(int(input("Please, define pen's size\n> ")))

        tess.forward(int(input("How many steps do you want the pen to make forward\n> ")))
        tess.left(int(input("Please, defined a angle to turn to the left\n> ")))
        tess.forward(int(input("How many steps do you want the pen to make forward\n> ")))
        tess.left(int(input("Please, defined the angle turn to the left\n> ")))
        tess.forward(int(input("How many steps do you want the pen to make forward\n> ")))
        tess.left(int(input("Please, defined the angle turn to the left\n> ")))
        tess.forward(int(input("How many steps do you want the pen to make forward\n> ")))
        print("What a wonderful draw you just made")
        wn.mainloop()
    pass
    if n == 3:
        import turtle

        wn = turtle.Screen()

        wn.bgcolor(str(input("Define the windows' blackgroud color")))
        wn.title("Tessa and Alex!")

        tessa = turtle.Turtle()
        tessa.color(str(input("Define Tessa's pen color")))
        tessa.pensize(int(input("Define Tessa's pen size")))

        alex = turtle.Turtle()
        alex.color(str(input("Define Alex's pen color")))
        alex.pensize(int(input("Define Alex's pen size")))

        tessa.forward(100)
        tessa.left(120)
        tessa.forward(100)
        tessa.left(120)
        tessa.forward(100)
        tessa.left(-60)
        tessa.forward(50)

        alex.forward(100)
        alex.left(90)
        alex.forward(100)
        alex.left(90)
        alex.forward(100)
        alex.left(90)
        alex.forward(100)
    pass
    if n == 4:
        for f in ["Zoe", "Joe", "Brad", "Angelica", "Zuki", "Thandi", "Paris"]:
            invite = "Hi " + f + ". Please come to my party on Saturday!"
            print(invite)
            # More code can follow here, of course!.
    pass
    if n == 5:
        import turtle

        wn = turtle.Screen()
        wn.bgcolor('black')
        alex = turtle.Turtle()
        for i in range(4):  # [0,1,2,3]:
            for c in ["yellow", "red", "purple", "blue"]:
                alex.color(c)
                alex.forward(50)
                alex.left(90)
    pass
    if n == 6:
        import turtle
        wn = turtle.Screen()
        alex = turtle.Turtle()
        #for i in range(4):
        clrs = ["yellow", "red", "purple", "blue"]  # Assign a list to a variables
        for c in clrs:
            alex.color(c)
            alex.forward(50)
            alex.left(90)
    pass
    if n == 7:
        import turtle

        wn = turtle.Screen()
        wn.bgcolor("lightblue")
        tessa = turtle.Turtle()
        tessa.shape("turtle")
        tessa.speed(3)
        tessa.penup()
        size = 20
        for i in range(5):
            clrs = ["red", "orange", "yellow", "green", "blue", "purple"]
            for c in clrs:
                tessa.color(c)
                tessa.stamp()
                size = size + 2
                tessa.forward(size)
                tessa.right(24)
        wn.mainloop()
    pass
    if n == 8:
        while True:
            m = int(input('Please, choose and write a number to select a program'
                          '\n  0: To go back.'
                          '\n -1: To quick\n'
                          '\n  1: Print 1000 times "We like Python\'s turtle!"'
                          '\n  2: Cellphone\'s attribute.'
                          '\n  3: Print the year\'s months'
                          '\n  4: Turn Tess left 3645 degrees.'
                          '\n  5: Print each numbr in a new line'
                          '\n  6: Print the square of each number in a new line'
                          '\n  7: Print the sum of all the elements on the list.'
                          '\n  8: Print the product of all the elements on the list.'
                          '\n 12: Draw a face clock'
                          '\n> '))
            if m == 0: break
            if m == -1:
                quit_program = True
                break
            if m == 1:  # We like Python's turtles!
                for x in range(1000):
                    print("We like Python's turtles!")
            if m == 2: # Give tree attributes and tree methods of your cellphone object.
                print('none')
                pass
            pass
            if m == 3: # Print the months of the year.
                months = [
                    "\n January is a month of the year"
                    "\n February is a month of the year"
                    "\n March is a month of the year"
                    "\n April is a month of the year"
                    "\n May is a month of the year"
                    "\n June is a month of the year"
                    "\n July is a month of the year"
                    "\n August is a month of the year"
                    "\n September is a month of the year"
                    "\n October is a month of the year"
                    "\n November is a month of the year"
                    "\n December is a month of th year"
                ]
                for x in months:
                    print(x)
            pass
            if m == 4: # Turn Tess 3645 degrees to the left.
                import turtle
                import time 

                print('Well, Tess is heading 0 and 3645 / 360 = 10.125',
                      '\nWhich means Tess wiil give 10.125 times a complete 360 degrees turn.',
                      '\nAnd, mathematically speaking:',
                      '\n   [(3645/360) - 10] * 360 = 45',
                      '\nor:'
                      '\n   (3645/360) / 10 = 45')
                time.sleep(1)

                print('First, let\'s make it turn 45 degrees.')
                print('Let\'s add a line to know where it was')
                wn = turtle.Screen()
                tess = turtle.Turtle()
                tess.left(45)
                
                tess.color('green')
                tess.forward(50)
                tess.forward(-50)
                time.sleep(1)

                print('Let\'s make it head to 0 again.')
                time.sleep(1)
                tess.left(-45)
                time.sleep(1)

                print('And now make it turn 3645 degrees.')
                time.sleep(1)
                tess.left(3645)
                
                print('Let\'s add another line to see whether or not',
                        '\nTess is heading the same direction')
                tess.color('blue')
                tess.forward(99)

                wn.mainloop()

                pass
            if m == 5: # Print each value on a new line.
                xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
                for xv in xs:
                    print(xv, end='\n')
            pass
            if m == 6: # Print the square of each value on a new line.
                xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
                for xv in xs:
                    print(xv**2, end='\n')
            pass
            if m == 7: # Print the total sum of the list.
                xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
                xi = 0
                for xv in xs:
                    xi = xi + xv
                print('The total sum is:', xi)
                pass
            if m == 8: # Print the total product of the list.
                xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
                xi = 1
                for xv in xs:
                    xi = xi * xv
                print('The total product is:', xi)
                pass
            if m == 12: # Draw a face clock.
                import turtle
                def draw_clock(T, radius, speed, angle):
                    """ I came back from cahper 04 to make a function. """
                    for a in range(12):
                        T.color('green')
                        T.shape('turtle')
                        T.shapesize(0.5)
                        T.penup()
                        T.speed(speed)
                        T.forward(radius)
                        T.stamp()
                        T.forward(-radius)
                        T.left(angle)
                    for x in range(12):
                        T.forward(radius - 15)
                        T.pendown()
                        T.color('green')
                        T.pensize(1)
                        T.forward(5)
                        T.penup()
                        T.forward(10 - radius)
                        T.left(angle)
                
                wn = turtle.Screen()
                wn.bgcolor('lightblue')
                wn.title('Tessa draws a clock')
                tessa = turtle.Turtle()
                draw_clock(tessa, 150, 5, 30)
                wn.mainloop
                pass
    pass
    if n == 9:
        import time

        seconds = int(input('Countdown seconds starting from...'))
        for countdown in reversed(range(seconds + 1)):
            if countdown > 0:
                print(countdown, '', sep='...', end='\n')
                time.sleep(1)
            else:
                print('Go!')
    pass
