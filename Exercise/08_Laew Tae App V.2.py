"""08 Laew Tae App V.2"""
class App:
    """App laew tae app"""
    def __init__(self, addmenu):
        """create self"""
        self.menulist = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.add = addmenu
    def list_foods(self):
        """show list foods"""
        return sorted(self.menulist)
    def add_food_item(self):
        """add food in list"""
        for _ in range(self.add):
            food = input()
            self.menulist.append(food)
def main():
    """laew tae app v2"""
    app = App(int(input()))
    app.add_food_item()
    print(app.list_foods())
main()
