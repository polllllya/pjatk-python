import turtle


def l_system_rules(rules):
    rule_dict = {
        'X': 'F+[[X]-X]-F[-FX]+X',  # P1 : X -> F+[[X]-X]-F[-FX]+X
        'F': 'FF'  # P2: F -> FF
    }
    next_rule = ''
    for character in rules:
        next_rule += rule_dict.get(character, character)

    print(next_rule)
    return next_rule


def draw_turtle(rules):
    stack = []

    window = turtle.Screen()
    window.bgcolor('black')

    myturtle = turtle.Turtle()
    myturtle.speed(3)
    myturtle.shape('classic')
    myturtle.shapesize(stretch_wid=0.5)
    myturtle.penup()
    myturtle.goto(-window.window_width() / 2 + window.window_height() / 2, -window.window_height() / 2)
    myturtle.pendown()
    myturtle.left(90)

    for character in rules:
        myturtle.color('green')

        if character == 'F':  # idź do przodu zostawiając ślad
            myturtle.forward(15)

        elif character == '+':
            myturtle.right(25)  # oznaczają obrót o 25 (w prawo)

        elif character == '-':
            myturtle.left(25)  # oznaczają obrót o 25 (w lewo)

        elif character == '[':
            angle = myturtle.heading()
            pos = [myturtle.xcor(), myturtle.ycor()]

            stack.append((angle, pos))  # odłóż wartości na stos

        elif character == ']':
            angle, pos = stack.pop()  # zdejmij ze stosu

            myturtle.setheading(angle)
            myturtle.penup()
            myturtle.goto(pos[0], pos[1])
            myturtle.pendown()

        # elif character == 'X':  symbol pomocniczy, nie jest do rysowania
        #     myturtle.forward(10)

    window.exitonclick()


def initialize():
    n = int(input("n >> "))
    rule = 'X'  # Słowo początkowe w=X
    for _ in range(n):
        rule = l_system_rules(rule)
    draw_turtle(rule)


initialize()