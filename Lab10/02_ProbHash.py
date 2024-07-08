"""Labs 10.02 - ProbHash Hashing"""
class ProbHash:
    """ProbHash"""
    def __init__(self, size):
        """__init__"""
        self.hash_table = [None for _ in range(size)]
        self.size = size # ขนาดตาราง hash
    def hash(self, key):
        """hash"""
        return key % self.size # return ช่องเก็บ adress
    def rehash(self, key):
        """rehash"""
        return key + 1
    def insert_data(self, std):
        """insert_data"""
        index = self.hash(std.get_std())
        if self.hash_table[index] == None: # ไม่มีข้อมูลใน adress นั้น
            self.hash_table[index] = std
            print("Insert %d at index %d" % (std.get_std(), index))
        else: # มีข้อมูลอยู่แล้วใน address
            index = self.rehash(index) # index = ช่องถัดไป adress
            while True:
                if index > self.size-1: # กรณี rehash แล้วเป็น ตน == size เนี่องจากถ้า size = 10 จะมีช่องแค่ 0-9 ไม่มี 10
                    for i in range(len(self.hash_table)): # ใช้ size ได้เหมือนกัน
                        if self.hash_table[i] == None:
                            self.hash_table[i] = std
                            print("Insert %d at index %d" % (std.get_std(), i))
                            return
                    print("The list is full. %d could not be inserted." % (std.get_std()))
                    break
                if self.hash_table[index] == None: # กรณี rehash แล้วว่างพอดี
                    self.hash_table[index] = std
                    print("Insert %d at index %d" % (std.get_std(), index))
                    break
                else:
                    index = self.rehash(index) # กรณี rehash ซ้ำอีกครั้ง
    def search_data(self, std_id):
        """search_data"""
        index = self.hash(std_id) # index = ค่า adress ของ std
        if self.hash_table[index] == None: # ไม่มีข้อมูล std
            print("%d does not exist." % (std_id))
            return None
        elif self.hash_table[index].get_std() == std_id: # มีข้อมูล std
            print("Found %d at index %d" % (std_id, index))
            return  self.hash_table[index]
        else: # ไม่มีข้อมูลตาม indexของ hashตรงๆ เช็คตัว rehash อีกที
            index = self.rehash(index)
            while True:
                if index > len(self.hash_table) - 1:
                    for i in range(len(self.hash_table)):
                        if self.hash_table[i] == None:
                            pass
                        elif self.hash_table[i].get_std() == std_id:
                            print("Found %d at index %d" % (std_id, i))
                            return  self.hash_table[i]
                    print("%d does not exist." % (std_id))
                    return None
                if self.hash_table[index] == None:
                    index = self.rehash(index)
                elif self.hash_table[index].get_std() == std_id:
                    print("Found %d at index %d" % (std_id, index))
                    return  self.hash_table[index]
                else:
                    index = self.rehash(index)
class Student():
    """student"""
    def __init__(self, std_id, name, gpa):
        """Constructor"""
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    def get_std(self):
        """get std"""
        return self.std_id
    def get_name(self):
        """get name """
        return self.name
    def get_gpa(self):
        """get gpa"""
        return self.gpa
    def print_detail(self):
        """details"""
        print(("ID: %d\nName: %s\nGPA: %.2f") % (self.std_id, self.name, self.gpa))
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()
