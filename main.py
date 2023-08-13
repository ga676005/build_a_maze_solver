from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    num_rows = 12
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_rows
    cell_size_y = (screen_y - 2 * margin) / num_cols
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()