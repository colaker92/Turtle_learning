import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")
drawing_board.title("Python Turtle")

# turtle_instance = turtle.Turtle() #bu turtledan bir tane olmasına gerek yok
# turtle_instance.forward(100) # Forward SAĞ

# turtle_instance2 = turtle.Turtle()
# turtle_instance2.left(180) # LEFT -> derece değerinden gidiyor 90' da dik
# turtle_instance2.forward(100) # Forward SAĞ

# Kare Çizme

'''
TEK TEK Yazılan kodlarla kare çizimi 
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
'''

'''
# kare çiziminin loop döngüsüyle yapımı mantık aynı sadece 1 kod satırı yazıyoruz loop 4 kez döndürüyor
turtle_instance = turtle.Turtle()

for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)

turtle.done()

'''


# Star yani YILDIZ çizimi

turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.left(36)
turtle_instance.backward(100)
turtle_instance.left(36)
turtle_instance.forward(100)
turtle_instance.left(36)
turtle_instance.backward(100)
turtle_instance.left(36)
turtle_instance.forward(100)
turtle_instance.left(36)

turtle.done()
