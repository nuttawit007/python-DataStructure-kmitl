"""04 Copy Stack"""
class ArrayStack:
    """Class ArrayStack use same class form 01"""
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
            return "Underflow: Cannot get stack top from an empty list"
        else:
            return self.data[-1]

    def get_size(self):
        """show sixe of data"""
        return self.size

    def print_stack(self):
        """print datck dat"""
        print(self.data)

    def clear_stack(self):
        """clear stack to empty"""
        self.size -= len(self.data)
        return self.data.clear()

    def get_data(self, input_num):
        """gat data you want"""
        return self.data[input_num]

def copy_stack(stack1, stack2):
    """function copy stack"""
    stack2.clear_stack()
    for _ in range(stack1.get_size()):
        stack2.push(stack1.get_data(_))

def print_status():
    """Print all stacks"""
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
    STACK4_.print_stack()
    print()


STACK1_ = ArrayStack()
STACK2_ = ArrayStack()


STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

# เพิ่มข้อมูลใน Stack1
for _ in range(int(input())):
    STACK1_.push(input())

# เพิ่มข้อมูลใน Stack2
for _ in range(int(input())):
    STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(
    STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_),
      TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))
