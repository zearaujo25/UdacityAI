from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    lines=[]
    r={}
    for x in range(0,9):
        y= x*9
        lines.append(grid[y:y+9])
        for z in range(0,9):
            r[row_units[x][z]]=lines[x][z]                
    return r

sudoku='..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid=grid_values(sudoku)
