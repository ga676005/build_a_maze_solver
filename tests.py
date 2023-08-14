import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_maze_total_cells(self):
        num_cols = 5
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)

        maze_total_cells = 0
        for i in range(m1._num_rows):
            for j in range(m1._num_cols):
                maze_total_cells += 1

        self.assertEqual(maze_total_cells, num_cols * num_rows)

    def test_maze_cells_are_not_visited_initially(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)

        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell._visited, False)


if __name__ == "__main__":
    unittest.main()
