from random import randint
import time


def main():
    sizes = [int(size) for size in input("Set sizes: ").split()]
    set1, set2, set3 = [long(size) for size in sizes]

    start_time = time.time()
    quadratic_done = quadratic_set_intersection(set1, set2, set3)
    quadratic_time = time.time() - start_time
    print(f"quadratic: Done in time {quadratic_time}")
    
    start_time = time.time()
    cubic_done = cubic_set_intersection(set1, set2, set3)
    cubic_time = time.time() - start_time
    print(f"cubic: Done in time {cubic_time}")


def long(size):
    return [randint(-size, size) for _ in range(size)]


def cubic_set_intersection(set1, set2, set3):
    for e1 in set1:
        for e2 in set2:
            for e3 in set3:
                if e1 == e2 == e3:
                    return False
    return True   


def quadratic_set_intersection(set1, set2, set3):
    for e1 in set1:
        for e2 in set2:
            if e1 == e2:
                for e3 in set3:
                    if e1 == e3:
                        return False
    return True


if __name__ == "__main__":
    main()
