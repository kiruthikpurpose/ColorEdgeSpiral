import turtle
import random

def draw_pattern():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "cyan"]

    for i in range(360):
        t.color(random.choice(colors))
        t.forward(i * 3 / 2)
        t.left(59)  # Angle for creating a spiral effect
        t.width(i * 3 / 100)  # Gradually increase the width of the line

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_pattern()
