from random import randint
import time


def main():
    size = int(input("Size: "))
    array = long(size)

    start_time = time.time()
    linear_done = linear_prefix_averages(array)
    linear_time = time.time() - start_time
    print(f"linear: Done in time {linear_time}")
    
    start_time = time.time()
    quadratic_done = quadratic_prefix_averages(array)
    quadratic_time = time.time() - start_time
    print(f"quadratic: Done in time {quadratic_time}")


def long(size):
    return [randint(-size, size) for _ in range(size)]


def quadratic_prefix_averages(list_):
    A = []
    length = len(list_)

    for i in range(length):
        sum_ = 0

        for j in range(i + 1):
            sum_ += list_[j]
        
        A.append(sum_/(i + 1))
    
    return A


def linear_prefix_averages(list_):
    if list_ is None or len(list_) == 1:
        return list_
    
    A = [list_[0]]

    for i in range(1, len(list_)):
        A.append((i*A[i - 1] + list_[i])/(i + 1))
    
    return A


if __name__ == "__main__":
    main()