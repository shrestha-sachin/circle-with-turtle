import turtle

To create a screen
screen = turtle.Screen()
screen.setup(width=1000, height=1000)

#To create a turtle object
tt = turtle.Turtle()
tt.speed(1)
tt.color("green")

#To ask radius from the user
radius = int(input("What is the length of a radius of circle?"))

#To find the perimeter of a circle
pi = 3.1415
circumference = 2 * pi * radius

#To make current point the center of a circle
tt.right(90)
tt.penup()
tt.forward(radius)  #To make a radius of a circle
tt.pendown()
tt.left(90)

num_sides = 360
angle = 360 / num_sides
for _ in range(num_sides):
    tt.forward(circumference/360)  #To divide the circumference by the number of sides
    tt.left(angle)

print("The circumference of a circle is", circumference)
