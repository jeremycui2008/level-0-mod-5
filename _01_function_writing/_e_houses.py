"""
Have the turtle draw a row of houses.
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
def pointyroof(height):
    bill.left(90)
    bill.forward(height)
    for i in range(2):
        bill.left(60)
        bill.forward(height/1.73)
    bill.left(60)
    bill.forward(height)
    bill.left(90)
    bill.forward(height)

def house(height):
    for i in range(4):
        bill.pencolor('black')
        bill.forward(height)
        bill.left(90)
    bill.forward(height)

if __name__  ==  '__main__':
    bill=turtle.Turtle()
    bill.penup()
    bill.goto(-470,-390)
    bill.pendown()
    bill.speed(3)
    for i in range (10):
        placeholder=simpledialog.askstring(None, prompt='do you want large house, medium house or little house?')
        if placeholder=='small':
            height=60
            house(height)
            pointyroof(height)
            bill.forward(height)
            bill.pencolor('green')
            bill.forward(130)
        if placeholder=='medium':
            height=120
            house(height)
            pointyroof(height)
            bill.forward(height)
            bill.pencolor('green')
            bill.forward(130)
        if placeholder=='large':
            height=250
            house(height)
            bill.forward(height)
            bill.pencolor('green')
            bill.forward(130)

    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    pass
