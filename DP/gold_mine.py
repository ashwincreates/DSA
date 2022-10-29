'''
    GOLD MINE

    Given a gold mine of n*m dimensions.
    Each field in this mine contains a positive integer which is the amount
    of gold in tons. Initially the miner is at first column but can be at any
    row. He can move only (right,right up,right down) that is from a given
    cell, the miner can move to the cell diagonally up towards the right or
    diagonally down towards the right. Find out maximum amount of gold he can
    collect.
'''

def collect_gold(mine, i, j):
    '''recursive function for gold mine problem'''
    if i < 0 or j < 0 or i == len(mine) or j == len(mine[0]):
        return 0
    max_gold = max({
        mine[i][j] + collect_gold(mine, i, j + 1),
        mine[i][j] + collect_gold(mine, i - 1, j + 1),
        mine[i][j] + collect_gold(mine, i + 1, j + 1),
    })
    return max_gold


gold_mine = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]
]
print(max([collect_gold(gold_mine, i, 0) for i in range(len(gold_mine))]))
