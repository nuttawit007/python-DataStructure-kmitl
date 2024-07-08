"""05 Parentheses Matching"""
class ArrayStack:
    """Class ArrayStack"""
    def __init__(self):
        """creat 2 attribute size = 0 and data = []"""
        self.size = 0
        self.data = []

    def push(self, input_data):
        """add data at the top of satck, push arg input data"""
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
        """remove data at the top of stack and show data that remove"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return "None"
        else:
            self.size -= 1
            return self.data.pop(-1)

    def get_size(self):
        """show sixe of data"""
        return self.size

def is_parentheses_matching():
    """check parentheses"""
    equation = input()
    stack = ArrayStack()
    for item in equation:
        if item == "(":
            stack.push(item)
        elif item == ")":
            stack.pop()
    if stack.get_size() == 0 and equation.count("(") == equation.count(")"):
        print("Parentheses in "+ equation +" are matched \nTrue")
    else:
        print("Parentheses in "+ equation +" are unmatched \nFalse")
is_parentheses_matching()
