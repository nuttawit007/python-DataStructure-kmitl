"""02 SinglyLinkList (Traversal and Insert Last)"""
class DataNode:
    """Create class DataNode"""
    def __init__(self, data=None):
        """Atrribute"""
        self.__data = data
        self.__next = None
    def get_data(self):
        """getter data"""
        return self.__data
    def set_data(self, __data):
        """set data"""
        self.__data = __data
    def get_next(self):
        """getter next"""
        return self.__next
    def set_next(self, __next):
        """set next"""
        self.__next = __next

class SinglyLinkedList:
    """Singly Linked List"""
    def __init__(self):
        """__init__"""
        self.count = 0
        self.head = None
    def traverse(self):
        """traverse"""
        if self.head == None:
            print("This is an empty list.")
        else:
            pos = self.head
            while True:
                if pos is None:
                    break
                if pos.get_next() == None:
                    print(pos.get_data(), end="")
                else:
                    print(pos.get_data(), end=" -> ")
                pos = pos.get_next()
    def insert_last(self, data):
        """insert_last"""
        next_node = DataNode(data)
        if self.head == None:
            self.head = next_node
        else:
            last_node = self.head
            while True:
                if last_node.get_next() is None:
                    break
                last_node = last_node.get_next()
            last_node.set_next(next_node)

LIST1_ = SinglyLinkedList()
for i in range(int(input())):
    LIST1_.insert_last(input())
LIST1_.traverse()
