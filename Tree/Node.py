'''
A class used to generate trees from array.
'''
class Node:
    def __init__(self, data, left=None, right=None):
        self.data: int = data
        self.left: Node = left
        self.right: Node = right

    @classmethod
    def from_list(self, values):
        self.data = values[0]
        arr = values[1:]
        queue = [self]
        while len(queue) > 0:
            curr = queue.pop(0)
            if len(arr) > 0 and arr[0] != -1 and arr[0] != "null":
                newNode = Node(arr[0])
                arr.pop(0)
                curr.left = newNode
                queue.append(curr.left)
            if len(arr) > 0 and arr[0] != -1 and arr[0] != "null":
                newNode = Node(arr[0])
                arr.pop(0)
                curr.right= newNode
                queue.append(curr.right)
        return self