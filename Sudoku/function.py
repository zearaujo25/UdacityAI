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
            if lines[x][z] != ".":
                r[row_units[x][z]]=lines[x][z]    
            else:
                r[row_units[x][z]]="123456789"
                
    return r

def get_peers(k):
    allpeers=[];
    for r in row_units:
        if k in r:
            allpeers=allpeers+r
            break
    for c in column_units:
        if k in c:
            allpeers=allpeers+c
            break

    for sq in square_units:
        if k in sq:
            allpeers=allpeers+sq
            break
            
    #removing duplicates 
    allpeers=sorted(list(set(allpeers)))
    
    return allpeers

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    pass
    units=[]
    clean=[]
    clean=values
    #checking all values in grid
    for k,v in values.items():
        #checking if it is a unknown value
        if len(v)>1:

            #getting all peers
            allpeers=get_peers(k)
            
           #getting off all the numbers 
            for p in allpeers:
                if len(values[p])==1 and values[p] in v and k!=p:
                    clean[k]=clean[k].replace(values[p],"")
            allpeers.clear()
    return values
from utils import *


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    
    for sq in square_units:
        for box in sq:
            if(len(values[box])>1):
                for digit in values[box]:
                    unique=True
                    for parser in sq:
                        if(parser==box):
                            continue
                        if (digit in values[parser]):
                            unique=False
                            continue
                    if unique:
                        values[box]=digit
    
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values=eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values=only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

sudoku='..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid=grid_values(sudoku)
display(reduce_puzzle(grid))

