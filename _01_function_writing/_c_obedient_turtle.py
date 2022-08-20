"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

def square(turtle_name):
    for i in range (4):
        turtle_name.right(90)
        turtle_name.forward(90)
def triangle(turtle_name):
    for i in range (3):
        turtle_name.right(120)
        turtle_name.forward(90)
def circle(turtle_name):
    turtle_name.circle(1000,5000,5000)


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.

    bill=turtle.Turtle()
    bill.speed(5)
    ron=simpledialog.askstring(title='shape', prompt='what shape do you want?')
    if ron=='square':
        square(bill)
    elif ron=='triangle':
        triangle(bill)
    elif ron=='circle':
        circle(bill)
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass
