# -----------------------------------------
# File Name : twodfigures.py
# Purpose   : User-defined module for
#             calculating area and perimeter
#             of different 2D figures.
# -----------------------------------------

import math   # Import math module for pi value

# -----------------------------
# Functions for Square
# -----------------------------

# Function to calculate area of a square
def square_area(side):
    return side * side

# Function to calculate perimeter of a square 
def square_perimeter(side):
    return 4 * side


# -----------------------------
# Functions for Circle
# -----------------------------

# Function to calculate area of a circle
def circle_area(radius):
    return math.pi * radius * radius

# Function to calculate circumference of a circle
def circle_perimeter(radius):
    return 2 * math.pi * radius


# -----------------------------
# Functions for Rectangle
# -----------------------------

# Function to calculate area of a rectangle
def rectangle_area(length, breadth):
    return length * breadth

# Function to calculate perimeter of a rectangle
def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


# -----------------------------
# Functions for Triangle
# -----------------------------

# Function to calculate area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Function to calculate perimeter of a triangle
def triangle_perimeter(a, b, c):
    return a + b + c
