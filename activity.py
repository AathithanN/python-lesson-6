import turtle 

turtle.screen() .bgcolour("blue")

sc=turtle.screen()
sc.setup(400,300)

turtle.title("This is Turtle")

board=turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1

    turtle.done()