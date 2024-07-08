"""01 Create BSTNode"""
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

def main():
    """main"""
    node = BSTNode()
    node.set_data(int(input()))
    print(node.get_data())
    print(node.get_left())
    print(node.get_right())
main()