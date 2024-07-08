"""05 Point"""
class Point:
    """class Point"""
    def __init__(self, var_x=0, var_y=0):
        """defult xy"""
        self.set_coordinates(var_x, var_y)

    def set_coordinates(self, var_x, var_y):
        """Set coordinates"""
        self.var_x = var_x
        self.var_y = var_y

    def get_coordinates(self):
        """check defult"""
        return (self.var_x, self.var_y)

    def calculate_distance(self, other_point):
        """Calulate distance"""
        return ((other_point.var_x - self.var_x)**2 + (other_point.var_y - self.var_y)**2) ** 0.5

def main():
    """05 point"""
    obj_boss = Point(float(input()), float(input()))
    obj_art = Point(float(input()), float(input()))
    print("%.2f" % obj_boss.calculate_distance(obj_art))
main()
