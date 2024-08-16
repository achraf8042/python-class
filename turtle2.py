from turtle import Screen , Turtle

window = Screen()
sam = Turtle()
window.title('octucode')
list_of_shaps = ('circle', 'triangle', 'square')
def square():
    for _ in range(4):
        sam.pensize(10)
        sam.shape('turtle')
        sam.pencolor('red')
        sam.forward(100)
        sam.left(90)


def triangle():
    for _ in range(3):
        sam.pensize(6)
        sam.shape('turtle')
        sam.pencolor('blue')
        sam.forward(150)
        sam.left(120)

def circle():
    sam.pensize(5)
    sam.pencolor('orange')
    sam.circle(60)

game_on = True
while game_on:
    user_choice = window.textinput('welcome', 'what do you want to draw')
    if user_choice in list_of_shaps:
        if user_choice == "circle".lower():
            circle()
        elif user_choice == 'triangle'.lower():
            triangle()
        elif user_choice == 'square'.lower():
            square()
    elif user_choice == 'exit'.lower():
        game_on = False
        window.clear()
        sam.color('black')
        sam.hideturtle()
        window.bgcolor('blue')
        sam.write('Press any key to exit', align='center', font=("arial", 24, "bold"))
        break
            



window.exitonclick()