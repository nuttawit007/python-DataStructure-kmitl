"""01 Create DataNode"""
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

def main():
    """Test"""
    data1 = DataNode()
    data1.set_data(input())
    print(data1.get_data())
    print(data1.get_next())
main()
