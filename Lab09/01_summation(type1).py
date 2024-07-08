""" 01 Summation(Type1) """
def summation1():
    """summation 1"""
    summation = 0
    for num in range(1, int(input())+1):
        summation += num
    print(summation)
summation1()
