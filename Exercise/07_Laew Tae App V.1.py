"""07 Laew Tae App V.1"""
class Menu:
    """Random menu list"""
    def __init__(self):
        """init self"""
        self.menulis = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.randoms = 1
    def random_foods(self):
        """random food"""
        return self.randoms
    def list_food(self):
        """list all menu"""
        return sorted(self.menulis)

def main():
    """main"""
    allfood = Menu()
    print(allfood.list_food())
main()
