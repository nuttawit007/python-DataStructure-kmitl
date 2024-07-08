""" 03 isIntersect """
import json
def is_intersect():
    """ intersected list """
    lista = json.loads(input())
    listb = json.loads(input())
    listc = json.loads(input())
    intersection_result = [value for value in lista if value in listb and value in listc]
    if len(intersection_result) == 0:
        print(False)
    else:
        print(True)
is_intersect()
