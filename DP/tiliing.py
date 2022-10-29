'''
    TILING PROBLEM

    Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways
    to tile the given board using the 2 x 1 tiles. A tile can either be placed
    horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile.
'''

def tiling(_n, area):
    '''recusive solution to tiling problem.'''
    if area == 0:
        return 1
    if area < 0:
        return 0
    no_of_ways = tiling(_n, area - 4) + tiling(_n, area - 2)
    return no_of_ways

n: int = 4
print(tiling(n, 2 * n))
