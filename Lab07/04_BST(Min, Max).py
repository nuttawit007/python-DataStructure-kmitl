"""02 Binary Search Tree (Preorder, Insert)"""
class BSTNode:
    """create BSTNode"""
    def __init__(self, data=int):
        """Attribute"""
        self.__data = data
        self.__left = None
        self.__right = None

    def get_data(self):
        """ return data"""
        return self.__data

    def set_data(self, __data):
        """ setter data """
        self.__data = __data

    def get_left(self):
        """ return left """
        return self.__left

    def set_left(self, __left):
        """ setter left """
        self.__left = __left

    def get_right(self):
        """ return right """
        return self.__right

    def set_right(self, __right):
        """ setter left """
        self.__right = __right

class BST():
    """ create BST """
    def __init__(self):
        """Attribute"""
        self.root = None
    def get_root(self):
        """ return root """
        return self.root
    def set_root(self, root):
        """ setter root """
        self.root = root
    
    def is_empty(self):
        return self.root is None
    
    def insert(self, data):
        """insert"""
        p_new = BSTNode(data)
        if self.root is None:
            self.root = BSTNode(data)
        else:
            prev = self.root
            while True:
                if p_new.get_data() >= prev.get_data() and prev.get_right() is None:
                    prev.set_right(p_new)
                    break
                elif p_new.get_data() < prev.get_data() and prev.get_left() is None:
                    prev.set_left(p_new)
                    break
                if p_new.get_data() >= prev.get_data():
                    prev = prev.get_right()
                else:
                    prev = prev.get_left()

    def preorder(self, root=None):
        """preorder"""
        if root != None:
            print("-> "+str(root.get_data()), end=" ")
            if root.get_left() != None:
                self.preorder(root.get_left())
            if root.get_right() != None:
                self.preorder(root.get_right())
        else:
            root = self.get_root()
            self.preorder(root)

    def inorder(self, root):
        """inorder"""
        if root == None:
            return
        self.inorder(root.get_left())
        print("-> " + str(root.get_data()), end=" ")
        self.inorder(root.get_right())

    def postorder(self, root):
        """postorder"""
        if root == None:
            return
        self.postorder(root.get_left())
        self.postorder(root.get_right())
        print("->", root.get_data(), end=" ")
    
    def traverse(self):
        """traverse"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder', end=" ")
        self.preorder(self.root)
        print()
        print('Inorder', end=" ")
        self.inorder(self.root)
        print()
        print('Postorder', end=" ")
        self.postorder(self.root)
        print()

    def _find_min(self, root):
        """min"""
        if self.is_empty():
            return None
        cur = root
        while cur.get_left():
            cur = cur.get_left()
        return cur.get_data()

    def find_min(self):
        """min"""
        return self._find_min(self.root)

    def find_max(self):
        """max"""
        return self._find_max(self.root)

    def _find_max(self, root):
        """max"""
        if self.is_empty():
            return None
        cur = root
        while cur.get_right():
            cur = cur.get_right()
        return cur.get_data()

def main():
    """code"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()
