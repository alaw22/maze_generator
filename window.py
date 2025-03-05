from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title("Maze Generator")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root,height=height,width=width)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False

    def draw_line(self,line:Line,fill_color:str):
        line.draw(self.canvas,fill_color=fill_color)
        

