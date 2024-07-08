"""04 Rectangle"""
class Rectangle:
    """Rectangle"""
    def __init__(self, height, width):
        """define var self"""
        self.height = height
        self.width = width
    def calculate_area(self):
        """return area rectangle"""
        return self.height * self.width
    def calculate_perimeter(self):
        """return perimeter value"""
        return (2*self.height) + (2*self.width)

def main():
    """04 Rectangle"""
    rectangle = Rectangle(float(input()), float(input()))
    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print("%.2f" % result)
main()
