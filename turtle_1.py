from turtle import Turtle, Screen

window = Screen()
window.bgcolor('blue')
window.setup(1000, 1000)
sam = Turtle()
sam.shape('turtle')
sam.pencolor('white')
sam.speed('fastest')
def draw_circle():
    for _ in range(10):
        sam.penup()
        sam.goto(-250, -250)
        sam.pendown()
        sam.circle(50)
        sam.left(360 / 10)

def draw_squer():
    for _ in range(10):
        sam.penup()
        sam.goto(0, 0)
        sam.pendown()
        sam.left(36)
        for _ in range(4):
            sam.forward(100)
            sam.left(90)

def draw_triangle():
    for _ in range(10):
        sam.penup()
        sam.goto(250, 250)    
        sam.pendown()
        sam.left(36)
        for _ in range(3):
            sam.forward(100)
            sam.left(120)

draw_circle()
draw_squer()
draw_triangle()

window.mainloop()