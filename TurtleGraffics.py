# SquareSpiral1.py - draws a square spiral
import turtle
from random import *
t = turtle.Pen()
moves = input("How many moves do you want Turtle to make?")
for x in range(int(moves)):
	t.forward(randint(10,100))
	t.left(90)
