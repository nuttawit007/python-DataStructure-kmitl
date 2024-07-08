"""Lab01 is even"""
def even():
    """is even"""
    number = input()
    even_num = ["0", "2", "4", "6", "8"]
    if number[-1] in even_num:
        print(True)
    else:
        print(False)
even()
