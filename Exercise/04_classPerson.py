"""04 Person"""
class Person:
    """class Person"""
    def __init__(self, name, age):
        """self"""
        self.name = "%s" % (name)
        self.age = age
    def get_details(self):
        """Meyhod detail"""
        return "%s, %d years old" % (self.name, self.age)
    def say_hello(self):
        """Method hello"""
        return "Hello, my name is %s!" % (self.name)
def main():
    """Create object"""
    obj = Person(input(), int(input()))
    print(obj.get_details())
    print(obj.say_hello())
main()
