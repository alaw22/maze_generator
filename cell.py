# top left corner is xmin,ymin
# bottom right corner is xmax, ymax
from point import Point
from window import Window
from line import Line

class Cell:
    def __init__(self,window:Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        
    def draw(self,x1,y1,x2,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line,fill_color='black')
        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self._win.draw_line(line,fill_color='black')
        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line,fill_color='black')
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self._win.draw_line(line,fill_color='black')

    def draw_move(self, to_cell, undo=False):

        # Consider making this a little more readable
        color = "red"
        if undo:
            color="gray"

        mid_point = Point((self._x2 + self._x1)//2,(self._y2 + self._y1)//2)

        mid_point2 = Point((to_cell._x2 + to_cell._x1)//2,(to_cell._y2 + to_cell._y1)//2)
        
        line = Line(mid_point,mid_point2)
        # Assume you can make move because making move should contain that logic
        self._win.draw_line(line,fill_color=color)