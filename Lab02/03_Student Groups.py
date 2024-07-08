"""Lab 02.03  Student Groups"""
class ArrayStack:
    """Arraystack"""
    def __init__(self):
        """__init__"""
        self.size = 0
        self.data = list()
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        """pop"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            self.size -= 1
            return self.data.pop(-1)

def main():
    """main"""
    group = int(input())
    total = int(input())
    mylist = list()
    stack = ArrayStack()
    # add data into stack
    for _ in range(total):
        stack.push(input())
    # create empty list in mylist as group
    for _ in range(group):
        mylist.append([])
    # add data in empty list in mylist
    for i in range(total):
        # what group taht data append
        possition = i % group
        pop = stack.pop()
        # add data in that group
        mylist[possition].append(pop)
    for i in range(group):
        print("Group %d: " % (i+1), end="")
        # print value in list by this pattern
        print(*mylist[i], sep=", ")
main()
