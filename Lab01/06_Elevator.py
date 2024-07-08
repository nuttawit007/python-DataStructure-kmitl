"""06 Elevator"""
class Elevator:
    """Create class elevator"""
    def __init__(self, max_floor):
        """defult vlaue"""
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """go to floor"""
        if floor > self.max_floor:
            print("Invalid Floor!")
        else:
            self.current_floor = floor

    def report_current_floor(self):
        """current floor"""
        print(self.current_floor)

def main():
    """06 Elevator"""
    elevator = Elevator(int(input()))
    while True:
        floor = input()
        if floor == "Done":
            break
        elevator.go_to_floor(int(floor))
    elevator.report_current_floor()
main()
