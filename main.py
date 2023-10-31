import math
figure = input("What figure do you want to calculate? :")
figures = ["square", "triangle", "circle", "rectangle", "elipse", "trapezoid"]

if figure in figures:
    print(f"The figure you chosen is available")
    if figure in figures and figure == figures[0]:
        a_square = int(input("type in measurement of a side: "))
        square_area = a_square * a_square
        print(f"The area of the square is: {square_area}")
    elif figure in figures and figure == figures[1]:
        a_triangle = int(input("type in measurement of a side: "))
        h = int(input("type in measurement of a height:"))
        triangle_area = (a_triangle * h) / 2
        print(f"The area of the square is: {triangle_area}")
    elif figure in figures and figure == figures[2]:
        r = int(input("type in measurement of a radius: "))
        circle_area = math.pi * (r * r)
        print(f"The area of the square is: {circle_area}")
    else:
        print("Sorry! There is no such option. ")
else:
    print("There is not this kind of figure in this program")
