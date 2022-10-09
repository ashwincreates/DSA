'''
    MORRIS INORDER TRAVERSAL

    A technique to traverse a tree without recursion or stack. This involves
    finding preceding inorder node and connecting it. This changes the structure of
    the tree but later restores it 

    Example tree:

            0
          / |
         /  |
        1   2
       /|  /|
      3 4 5 6
'''

from Node import Node

def morris_traveral_inorder(root):
    curr: Node = root;
    while curr != None:
        if curr.left == None:
            print(curr.data)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right != None and pre.right != curr:
                pre = pre.right
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                print(curr.data)
                curr = curr.right

def morris_traveral_preorder(root):
    curr: Node = root;
    while curr != None:
        if curr.right == None:
            print(curr.data)
            curr = curr.left
        else:
            pre = curr.right
            while pre.left != None and pre.left != curr:
                pre = pre.left
            if pre.left is None:
                pre.left = curr
                curr = curr.right
            else:
                pre.left = None
                print(curr.data)
                curr = curr.left

morris_traveral_inorder(Node.from_list([15, 1, 4, 5, 2, 3, 6, 7, -1, -1, -1, -1, -1, -1, -1, -1]))