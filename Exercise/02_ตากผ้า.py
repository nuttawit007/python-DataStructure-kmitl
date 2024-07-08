"""02 ตากผ้า"""
def main():
    """ตากผ้า"""
    place = input()
    minute = float(input())
    if place == "Indoor" and minute/60 >= 8:
        print(True)
    elif place == "Outdoor" and minute/60 >= 4:
        print(True)
    else:
        print(False)
main()
