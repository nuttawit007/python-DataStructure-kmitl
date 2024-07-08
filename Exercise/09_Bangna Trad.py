"""09 Bangna Trad"""
def main():
    """Final PSCP"""
    road_pillar = float(input())
    if 0 <= road_pillar <= 5.032:
        print("Bangkok")
    elif 5.032 < road_pillar <= 35.477:
        print("Samut Prakarn")
    elif 35.477 < road_pillar <= 52.9:
        print("Chachoengsao")
    elif 52.9 < road_pillar <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")
main()
