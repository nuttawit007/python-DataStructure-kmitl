"""01 Stack (Create Stack)"""
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

    def pop(self):#ไม่ได้รับค่าอะไรใส่แค่ self
        """remove data at the top of stack and show data that remove"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return "None"
        else:
            self.size -= 1
            return self.data.pop(-1)

    def is_empty(self):
        """if strack empty >> False, else >> True"""
        if self.size == 0:
            return True
        else:
            return False

    def get_stack_top(self):
        """show data at the top of stack"""
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return "None"
        else:
            return self.data[-1]

    def get_size(self):
        """show sixe of data"""
        return self.size

    def print_stack(self):
        """print datck dat"""
        print(self.data)

STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()
print(STACK_.get_size())

VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())

print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)
