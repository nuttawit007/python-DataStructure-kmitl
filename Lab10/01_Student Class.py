""" 01 Student Class """
class Student:
    """ class Student """
    def __init__(self, std_id, name, gpa):
        """ Atrribute """
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self) -> int:
        """ getter Student id"""
        return self.std_id

    def get_name(self) -> str:
        """getter Student name"""
        return str(self.name)

    def get_gpa(self) -> float:
        """getter Student float"""
        return str(self.gpa)

    def print_detail(self):
        """print detail"""
        print("ID: " + str(self.std_id))
        print("Name: " + self.name)
        print("GPA: " + "%.2f" % self.gpa)

def main(text_in):
    """main"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())
