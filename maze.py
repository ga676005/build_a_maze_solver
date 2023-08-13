import random
import time
from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            self._cells.append(row)
            for j in range(self._num_cols):
                c = Cell(self._win)
                row.append(c)

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

        self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._cell_size_x * i + self._x1
        y1 = self._cell_size_y * j + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        # print("draw", {" x1": x1, " x2": x2, " y1": y1, " y2": y2, "i": i, "j": j})
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.001)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True

        while True:
            possible_direction = []

            if i - 1 >= 0 and self._cells[i - 1][j]._visited == False:
                possible_direction.append("left")

            if (
                i + 1 <= (self._num_rows - 1)
                and self._cells[i + 1][j]._visited == False
            ):
                possible_direction.append("right")

            if j - 1 >= 0 and self._cells[i][j - 1]._visited == False:
                possible_direction.append("top")

            if (
                j + 1 <= (self._num_cols - 1)
                and self._cells[i][j + 1]._visited == False
            ):
                possible_direction.append("bottom")

            if len(possible_direction) == 0:
                self._draw_cell(i, j)
                return

            direction = random.choice(possible_direction)
            next_cell_i = 0
            next_cell_j = 0

            if direction == "left":
                next_cell_i = i - 1
                next_cell_j = j
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell_i][next_cell_j].has_right_wall = False

            elif direction == "right":
                next_cell_i = i + 1
                next_cell_j = j
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell_i][next_cell_j].has_left_wall = False

            elif direction == "top":
                next_cell_i = i
                next_cell_j = j - 1
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell_i][next_cell_j].has_bottom_wall = False

            elif direction == "bottom":
                next_cell_i = i
                next_cell_j = j + 1
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell_i][next_cell_j].has_top_wall = False

            self._break_walls_r(next_cell_i, next_cell_j)
