from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_coord = 0
        y_coord = 0
        for turtle in range(0, 3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x_coord, y_coord)
            # turtle.shapesize(stretch_wid=20, stretch_len=20)
            self.segments.append(turtle)
            x_coord -= 20

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(self.segments[-1].position())
        # turtle.shapesize(stretch_wid=20, stretch_len=20)
        self.segments.append(turtle)

    def move(self):
        for turtle_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[turtle_num - 1].xcor()
            new_y = self.segments[turtle_num - 1].ycor()
            self.segments[turtle_num].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
