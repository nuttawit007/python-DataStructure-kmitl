"""05 Person V2"""
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

class Project:
    """Class Project"""
    def __init__(self, name, age):
        """self"""
        self.name = name
        self.age = age
    def show_projectname(self):
        """show project name"""
        return "Hello There! This is %s" % (self.name)
    def show_member(self):
        """show all member"""
        return "This project has %d members" % (self.age)

def main():
    """Create object"""
    project_name, project_member = input(), int(input())
    obj_prject = Project(project_name, project_member)
    print(obj_prject.show_projectname())
    print(obj_prject.show_member())
    all_member = sorted([[input(), int(input())] for _ in range(project_member)])
    for i in range(project_member):
        obj_person = Person(all_member[i][0], all_member[i][1])
        print(obj_person.say_hello())
main()
