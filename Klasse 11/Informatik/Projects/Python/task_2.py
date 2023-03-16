import tkinter
import math

stage = tkinter.Tk()

class Turtle():
    def __init__(self) -> None:
        self.canvas = tkinter.Canvas()
        self.x=200
        self.y=80
        self.a=0

    def move(self, l):
        dx = math.cos(self.a * math.pi / 180) * l
        dy = math.sin(self.a * math.pi / 180) * l
        print(dx, dy)
        self.canvas.create_line(self.x, self.y, self.x+dx, self.y+dy)
        self.x+=dx
        self.y+=dy
        
    def rotate(self, p):
        self.a+=p

turtle = Turtle()
for _ in range(8):
    turtle.rotate(45)
    turtle.move(50)
turtle.canvas.pack()

stage.mainloop()