'''
    FRIEND PAIR UP

    Given n friends, each one can remain single or can be paired up
    with some other friend. Each friend can be paired only once. Find
    out the total number of ways in which friends can remain single or
    can be paired up.
'''

def pair_up(n):
    '''recursive function for friend pairing up.'''
    if n == 0:
        return 1
    # Either n + 1th friend can go as a single member or group
    # with any of the remaining groups
    return pair_up(n - 1) + (n - 1) * pair_up(n - 2)
