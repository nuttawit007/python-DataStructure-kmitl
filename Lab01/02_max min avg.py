"""02 Max Min Avg"""
import json
def highest(lis_num):
    """Find Max value"""
    highest_num = lis_num[0]
    for num in range(1, len(lis_num)):
        if lis_num[num] > highest_num:
            highest_num = lis_num[num]
    return "(" + str(round(highest_num, 2)) + ","

def lowest(lis_num):
    """Find Min value"""
    lowest_num = lis_num[0]
    for num in range(1, len(lis_num)):
        if lis_num[num] < lowest_num:
            lowest_num = lis_num[num]
    return str(round(lowest_num, 2)) + ","

def average(lis_num):
    """Find Average value"""
    total = 0
    for num in lis_num:
        total += num
    total = total/len(lis_num)
    return str(round(total, 2)) + ")"

def main():
    """Max Min Avg"""
    lis_num = json.loads(input())
    print(highest(lis_num), lowest(lis_num), average(lis_num))
main()
