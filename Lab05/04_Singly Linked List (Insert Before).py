"""04 SinglyLinkList (Insert Before)"""
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
        node = DataNode(data)
        if self.head == None:
            self.head = node
        else:
            last_node = self.head
            while True:
                if last_node.get_next() is None:
                    break
                last_node = last_node.get_next()
            last_node.set_next(node)

    def insert_front(self, data):
        """insert front"""
        node = DataNode(data)
        node.set_next(self.head)
        self.head = node

    def insert_before(self, node, data):
        """insert before"""
        new_data = DataNode(data)
        check = self.head
        while True:
            if check == None: # empty Linklist
                break
            if check.get_data() == node:
                check = True
                break
            check = check.get_next()
        if check != True:
            print("Cannot insert, %s does not exist." % (node))
        elif self.head.get_data() == node:
            new_data.set_next(self.head)
            self.head = new_data
        else:
            pnew = self.head
            while True:
                if pnew.get_next().get_data() == node:
                    new_data.set_next(pnew.get_next())
                    pnew.set_next(new_data)
                    break
                pnew = pnew.get_next()

def main():
    """main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()


main()
