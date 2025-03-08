from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    height = 600
    width = 800
    win = Window(width,height)

    limiting_length = min(height,width)

    cell_size = 30
    x_offset = cell_size//2 if width < height else cell_size//2 + (width - height)//2
    y_offset = cell_size//2 if height < width else cell_size//2 + (height - width)//2

    maze = Maze(x_offset,
                y_offset,
                (limiting_length-cell_size)//cell_size,
                (limiting_length-cell_size)//cell_size,
                cell_size,
                cell_size,
                win)
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()
