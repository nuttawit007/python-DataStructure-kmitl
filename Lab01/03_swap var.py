"""03 swap var"""
def main():
    """swap var"""
    text_in = input()
    values = tuple(map(float, text_in.strip('()').split(', ')))
    num1, num2 = str(values[1]), str(values[0])
    print("("+num1+", "+num2+")")
main()
