'''
    Boolean Parenthesis
    Return the numbers for ways to get True from a boolean expr
'''


def bool_parenthesis(s, i, j, res) -> int:
    if i > j:
        return 0
    if i == j:
        if res is True:
            return int(s[i] == 'T')
        else:
            return int(s[i] == 'F')

    ans = 0
    for k in range(i + 1, j, 2):
        lt = bool_parenthesis(s, i, k - 1, True)
        lf = bool_parenthesis(s, k + 1, j, False)

        rt = bool_parenthesis(s, i, k - 1, True)
        rf = bool_parenthesis(s, k + 1, j, False)

        if s[i] == '^':
            if res is True:
                ans += lf * rt + rf * lt
            else:
                ans += lt * rt + lf * rf
        elif s[i] == '&':
            if res is True:
                ans += lt * rt
            else:
                ans += lt * lf + rf * lf + lf * rt
        else:
            if res is True:
                ans += lt * rf + lf * rt + lt * rt
            else:
                ans += lf * rf

    return ans


expr = "T&F|T"
print(bool_parenthesis(expr, 0, len(expr), True))
