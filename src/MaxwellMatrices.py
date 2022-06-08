from operator import add as addition
from operator import sub as substraction

def add(list1, list2):
    return list(map(addition, list1, list2))
def sub(list1, list2):
    return list(map(substraction, list1, list2))