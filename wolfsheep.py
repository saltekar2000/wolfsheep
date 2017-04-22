import itertools as it

# constants
GRIDSZ = 5

def reachable( pos, grid_size ):
    ''' 
    Find all grid positions reachable from given position using motion along
    vertical, horizontal and diagonal lines.
    '''
    i0,j0 = pos
    rset = set()
    # horizontal line
    for i in range(grid_size):
        rset.add((i,j0))
    # vertical line
    for j in range(grid_size):
        rset.add((i0,j))
    # diagonal up (left->right) line
    if i0-j0 >= 0:
        istart,jstart = (i0-j0,0)
        for k in range(grid_size):
            if k+istart < grid_size:
                rset.add((k+istart,k+jstart))
    else:
        istart,jstart = (0,j0-i0)
        for k in range(grid_size):
            if k+jstart < grid_size:
                rset.add((k+istart,k+jstart))
    # diagonal down (left->right) line
    if i0+j0 < grid_size:
        istart,jstart = (0,i0+j0)
        for k in range(grid_size):
            if jstart-k >= 0:
                rset.add((istart+k,jstart-k))                           
    else:
        istart,jstart = (i0+j0-(grid_size-1),grid_size-1)
        for k in range(grid_size):
            if istart+k < grid_size:
                rset.add((istart+k,jstart-k))
    return rset


def print_grid( rset, grid_size, symbol = '*' ):
    '''
    Print out grid in a pretty format
    '''
    grid = [['-']*grid_size for _ in range(grid_size)]
    for pos in rset:
        i,j = pos
        grid[i][j] = symbol
    for i in range(grid_size):
        print(''.join(grid[i]))
    return
    
def solve_puzzle(nsheep, nwolf, grid_size):
    '''
    Solve wolf-sheep puzzle by exhaustively trying all possible placements of sheep.
    '''
    for trial in it.combinations(it.product(range(grid_size),range(grid_size)),nsheep):
        rset = set()
        for pos in trial:
            rset.update(reachable(pos,grid_size))
        if grid_size*grid_size - len(rset) >= nwolf:
            print('\n\n')
            print_grid(trial,grid_size,'S')
