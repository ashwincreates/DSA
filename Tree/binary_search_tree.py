class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.val: int = data
        self.left: BSTNode = left
        self.right: BSTNode = right

class BST:
    def __init__(self):
        self._root: BSTNode = None
        self._size: int = 0
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        pass

    def __contains__(self, val):
        return self.__bstSearch__(self.root, val)

    def _bstSearch_(self, node: BSTNode, val: int):
        if node is None:
            return False
        if node.val == val:
            return True
        elif node.val < val:
            return self.__bstSearch__(node.left, val)
        else:
            return self.__bstSearch__(node.right, val)
    
    def add(self, val: int):
        if val not in self:
            self._bstInsert(val)
            self._size += 1
    
    def _bstInsert_(self, node: BSTNode, val: int):
        if node == None:
            node = BSTNode(val)
        elif val < node.val:
            self._bstInsert_(node.left, val)
        else:
            self._bstInsert_(node.right, val)
    
    def remove(self, val: int):
        if val in self:
            self._root = self._bstRemove_(self._root, val)
            self._size -= 1
    
    def _bstMinimum_(self, node):
        pass
    
    def _bstRemove_(self, node: BSTNode, val: int):
        if node == None:
            return None
        elif node.val < val:
            node = self._bstRemove_(node.left, val)
        elif node.val > val:
            node = self._bstRemove_(node.right, val)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None or node.right is None:
                if node.left is None:
                    return node.right
                else:
                    return node.left
            else:
                pass
            