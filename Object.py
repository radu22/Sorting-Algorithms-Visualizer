import pygame as py

x_offset = 10
y_offset = 0
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255,255,255)

class Rectangle:
    x = 10
    y = 1
    width = 10
    height = 10
    color = red
    counter=0

    def __init__(self, height, counter):
        self.height = height
        self.x = (5 + self.width) * counter
        self.counter = counter

    def draw(self, screen, counter):
        py.draw.rect(screen, self.color, py.Rect((5 + self.width) * counter + x_offset, self.y + y_offset, self.width, self.height))

    def getHeight(self):
        return self.height

    def get_x(self):
        return self.x

    def change_x(self, x):
        self.x = x

    def change_h(self, h):
        self.height = h

    def swap(self, other):
        aux = self.x
        self.x = other.x
        other.x = aux

    def select(self):
        self.color = green

    def deselect(self):
        self.color = red

    def lowest_value(self):
        self.color = blue

    def to_be_inserted(self):
        self.color = white