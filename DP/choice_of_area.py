'''
    CHOICE OF AREA

    Consider a game, in which you have two types of powers, A and B and there are 3
    types of Areas X, Y and Z. Every second you have to switch between these areas,
    each area has specific properties by which your power A and power B increase or
    decrease. We need to keep choosing areas in such a way that our survival time is
    maximized. Survival time ends when any of the powers, A or B reaches less than 0.
'''

def choice_of_area(X, Y, Z, A, B, last, should_go):
    if not should_go:
        return 0
    if A <= 0 or B <= 0:
        return 0
    count = 1 + max([
        choice_of_area(X, Y, Z, A + X[0], B + X[1], 0, last != 0),
        choice_of_area(X, Y, Z, A + Y[0], B + Y[1], 1, last != 1),
        choice_of_area(X, Y, Z, A + Z[0], B + Z[1], 2, last != 2)
        ])
    return count

print(max([
    choice_of_area((5, 2), (-5, -10), (-20, 5), 20, 8, 0, True),
    choice_of_area((3, 2), (-5, -10), (-20, 5), 20, 8, 1, True),
    choice_of_area((3, 2), (-5, -10), (-20, 5), 20, 8, 2, True)
]))