from graphics import Line, Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        left_line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(left_line, "black" if self.has_left_wall else "white")

        right_line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(right_line, "black" if self.has_right_wall else "white")

        top_line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(top_line, "black" if self.has_top_wall else "white")

        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(bottom_line, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        center_x_of_to_cell = (to_cell._x1 + to_cell._x2) / 2
        center_y_of_to_cell = (to_cell._y1 + to_cell._y2) / 2
        line = Line(
            Point(center_x, center_y), Point(center_x_of_to_cell, center_y_of_to_cell)
        )
        color = "red" if undo is False else "black"
        self._win.draw_line(line, color)

    # def draw_move(self, to_cell, undo=False):
    #     if self._win is None:
    #         return
    #     x_mid = (self._x1 + self._x2) / 2
    #     y_mid = (self._y1 + self._y2) / 2

    #     to_x_mid = (to_cell._x1 + to_cell._x2) / 2
    #     to_y_mid = (to_cell._y1 + to_cell._y2) / 2

    #     fill_color = "red"
    #     if undo:
    #         fill_color = "gray"

    #     # moving left
    #     if self._x1 > to_cell._x1:
    #         line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
    #         self._win.draw_line(line, fill_color)
    #         line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
    #         self._win.draw_line(line, fill_color)
    #         print("move left")

    #     # moving right
    #     elif self._x1 < to_cell._x1:
    #         line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
    #         self._win.draw_line(line, fill_color)
    #         line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
    #         self._win.draw_line(line, fill_color)
    #         print("move right")

    #     # moving up
    #     elif self._y1 > to_cell._y1:
    #         line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
    #         self._win.draw_line(line, fill_color)
    #         line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
    #         self._win.draw_line(line, fill_color)
    #         print("move up")

    #     # moving down
    #     elif self._y1 < to_cell._y1:
    #         line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
    #         self._win.draw_line(line, fill_color)
    #         line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
    #         self._win.draw_line(line, fill_color)
    #         print("move down")
