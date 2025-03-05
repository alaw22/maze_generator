from window import Window
from point import Point
from line import Line


def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(200,200),Point(300,200)),fill_color="black")
    win.draw_line(Line(Point(300,200),Point(300,300)),fill_color="black")
    win.draw_line(Line(Point(300,300),Point(200,300)),fill_color="black")
    win.draw_line(Line(Point(200,300),Point(200,200)),fill_color="black")
        


    win.wait_for_close()

if __name__ == "__main__":
    main()
