from math import pi



figure = input()
area = 0

if figure == "square":
    side_square = float(input())
    area = side_square * side_square
if figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
if figure == "circle":
    r = float(input())
    area = r * r * pi
if figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2

print(f"{area:.3f}")
