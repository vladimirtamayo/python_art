import turtle

tt = turtle.Turtle()
turtle.bgcolor('black')

tt.shape('turtle')

tt.color('yellow')
for i in range(4):
    tt.forward(300)
    tt.right(90)

tt.color('green')
for i in range(3):
    tt.forward(300)
    tt.right(120)

turtle.done()
