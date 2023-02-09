from turtle import Turtle
MOVE_FORWARD = 10
POSITION = [(0,0), (-10,0), (-20,0)]
class Snake:

    def __init__(self) -> None:

        self.snakes = []
        self.creat_snake()
        self.head = self.snakes[0]
    
    def creat_snake(self):
        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, position):
            snake = Turtle(shape="square")
            snake.penup()
            snake.shapesize(stretch_len=0.5,stretch_wid=0.5)
            snake.goto(position)
            snake.color("white")
            self.snakes.append(snake)


    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def reset(self):

        for i in self.snakes:
            i.goto(1000,1000)

        self.snakes.clear()
        self.creat_snake()
        self.head = self.snakes[0]



    def move(self):
        for seg in range(len(self.snakes)-1, 0, -1):
            x_pos = self.snakes[seg-1].xcor()
            y_pos = self.snakes[seg-1].ycor()
            self.snakes[seg].goto(x_pos, y_pos)

        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)