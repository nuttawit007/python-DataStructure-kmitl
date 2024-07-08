""" 04 Calculator """
def main(number):
    """ Calculator """
    if number == 1:
        print(1)
    else:
        express = number
        result = 0
        amount = len(str(number))
        for i in range(1, amount):
            result += i*(9*(10**(i-1)))
        result += amount*(number+1-10**(amount-1))
        result += express
        print(result)
main(int(input()))
