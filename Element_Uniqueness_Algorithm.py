from random import randint
import time
from collections import defaultdict


def main():
    size = int(input("Size: "))
    list_ = long(size)

    start_time = time.time()
    linear_done = linear_element_uniqueness(list_)
    linear_time = time.time() - start_time
    print(f"linear: Done in time {linear_time}")

    start_time = time.time()
    quadratic_done = quadratic_element_uniqueness(list_)
    quadratic_time = time.time() - start_time
    print(f"quadratic: Done in time {quadratic_time}")
    

def long(size):
    return [randint(-size*100, size*100) for _ in range(size)]


def quadratic_element_uniqueness(list_):
    length = len(list_)
    for i in range(length):
        for j in range(i + 1, length):
            if list_[i] == list_[j]:
                return False
    return True


def linear_element_uniqueness(list_):
    dict_ = defaultdict(int)

    for element in list_:
        dict_[element] += 1
    
    for e in dict_.values():
        if e > 1:
            return False
    return True


if __name__ == "__main__":
    main()
