import turtle


def getSideLength():
    """
    This function is here to ask the user for the size of the image/flower.
    :return: This return returns the size that the user has just replied with back to the main and converts their input
    to an int.
    """
    side_length = input("What do you want the side length to be?")

    return int(side_length)


def getCenterColor():
    """
    This function is here to ask the user for the center petal color
    :return: This return returns the center color that was just recieved back to the main so that the rest of the
    program knows the center color.
    """
    center_color = input("What do you want the center petal color to be?")

    return center_color


def getPetalColor():
    """
    This function is here to ask the user for the remaining petals color.
    :return: This return returns the petal color that was just recieved and sends it to the main so that the rest of
    the program knows the remaining petals color.
    """
    petal_color = input("What do you want the petal color to be?")

    return petal_color


def draw_hexagon(size, color):
    """
    This function is drawing the hexagon itself.
    :param size: Uses the param size defined in getSideLength and main.
    :param color: Uses the param color defined in getCenterColor and main.
    :return: Returns the parameters
    """
    turtle.begin_fill()
    # Function that draws octagon and makes it a specific color
    for x in range(6):
        turtle.color(color)
        turtle.fd(size)
        turtle.rt(60)
    turtle.end_fill()
    turtle.speed(100)


def turn_turtle(size):
    """
    This function is here to turn the turtle after drawing a hexagon.
    :param size: Uses the size param to know how far forward to go before turning.

    """
    turtle.fd(size)
    turtle.left(60)


def main():
    color = getCenterColor()
    size = getSideLength()
    petal_color = getPetalColor()
    turtle.goto(0, 0)
    turtle.left(120)
    draw_hexagon(size, color)
    turtle.right(120)
    turn_turtle(size)
    draw_hexagon(size, petal_color)
    for y in range(5):
        turn_turtle(size)
        draw_hexagon(size, petal_color)

main()
turtle.exitonclick()
