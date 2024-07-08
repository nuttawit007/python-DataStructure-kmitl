"""03 Sorting Name"""
def bubble_strings(string_list):
    """Sort string by use bubble sort"""
    lenght = len(string_list)
    for i in range(lenght - 1):
        for j in range(0, lenght - i - 1):
            if string_list[j] > string_list[j + 1]:
                string_list[j], string_list[j + 1] = string_list[j + 1], string_list[j]
    return string_list

def main(quan):
    """Sorting Name"""
    all_mem = [input() for _ in range(quan)]
    for member in bubble_strings(all_mem):
        print(member)
main(int(input()))
