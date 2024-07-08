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
def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()