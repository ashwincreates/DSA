from Node import Node

'''
                    15
                   /  \
                  4    4
'''

def solve(A, B):
        curr = A
        stack = [A]
        m = {}
        while len(stack) > 0:
            if curr.data == B:
                break
            if curr.left != None and curr.data not in m:
                stack.append(curr.left)
                curr = curr.left
            elif curr.right != None and curr.data not in m:
                stack.append(curr.right)
                curr = curr.right
            else:
                curr = stack[-1]
                m[curr.data] = True
                stack.pop()
        return [i.data for i in stack]

print(*solve(Node.from_list([15, 1, 4, 5, 2, 3, 6, 7, -1, -1, -1, -1, -1, -1, -1, -1]), 7))