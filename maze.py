from cell import Cell
from point import Point
import time
import random

class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))

            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    
    def _draw_cell(self,i,j):
        if self._win is None:
            return
        
        top_left = Point(self._x1 + i*self._cell_size_x, self._y1 + j*self._cell_size_y)
        bottom_right = Point(top_left.x + self._cell_size_x, top_left.y + self._cell_size_y)
        self._cells[i][j].draw(top_left.x,top_left.y,bottom_right.x,bottom_right.y)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)


    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check right adjacent cell
            if i + 1 < self._num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))

            # Check left adjacent cell
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))

            # Check bottom adjacent cell
            if j + 1 < self._num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))

            # Check top adjacent cell
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))

            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return

            random_idx = random.randrange(len(to_visit))
            random_dir = to_visit[random_idx]

            # knock down walls
            if random_dir[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            elif random_dir[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            elif random_dir[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            elif random_dir[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            else:
                raise Exception("The current cell is equal to the random cell this should never happen")    
            
            self._break_walls_r(*random_dir)
    
    def solve(self,i=0,j=0):
        return self._solve_r(i,j)

    def _solve_r(self,i,j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        directions = [(i+1,j), # right
                      (i,j+1), # down
                      (i-1,j), # left
                      (i,j-1)] # up

        for col, row in directions:
            try:
                next_cell = self._cells[col][row]
            except IndexError:
                continue

            if col > i:   # right
                if not next_cell.has_left_wall and not current_cell.has_right_wall and not next_cell.visited:
                    current_cell.draw_move(next_cell)
                    if self._solve_r(col,row):
                        return True

                    current_cell.draw_move(next_cell,undo=True)

            elif col < i: # left 
                if not next_cell.has_right_wall and not current_cell.has_left_wall and not next_cell.visited:
                    current_cell.draw_move(next_cell)
                    if self._solve_r(col,row):
                        return True

                    current_cell.draw_move(next_cell,undo=True)
            elif row > j: # down
                if not next_cell.has_top_wall and not current_cell.has_bottom_wall and not next_cell.visited:
                    current_cell.draw_move(next_cell)
                    if self._solve_r(col,row):
                        return True

                    current_cell.draw_move(next_cell,undo=True)

            elif row < j: # up
                if not next_cell.has_bottom_wall and not current_cell.has_top_wall and not next_cell.visited:
                    current_cell.draw_move(next_cell)
                    if self._solve_r(col,row):
                        return True

                    current_cell.draw_move(next_cell,undo=True)
            else:
                raise Exception("Impossible direction to travel")
            
        return False

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    
