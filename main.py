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

'''
# Star yani YILDIZ çizimi

# uzun yolu

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
'''
''' 
# loop ile yapımı test
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(100)
turtle.done()
'''

'''
# polygon yapımı

# matematik formülü ile çizim

turtle_instance = turtle.Turtle()
num_sides = 5 # kaç kenarlı polygon çizeceksek o değeri atıyoruz
angle = 360.0 / num_sides # 360.0 -> derece ifadesi / num_sides -> kenar sayısı
side_lenght = 100 # ne kadar ileri gideceği

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_lenght)
turtle.done()
'''





