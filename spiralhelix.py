import turtle


turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Turtle Python")


turtle_instance = turtle.Turtle()
turtle_instance.color("red")
turtle_color = ["red","purple","yellow","orange","green","blue"]

for x in range(10):
    turtle_instance.color(turtle_color[x % 6])
    turtle_instance.circle(10 * x) # circle bizden yarı çap istiyor tanımlı formülde böyle istiyor r = 50 vermiş olduk biz
    turtle_instance.circle(-10 * x)
    turtle_instance.left(x)


turtle.mainloop()
# turtle.done()


