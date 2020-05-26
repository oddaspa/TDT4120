#!/usr/bin/python3
from sys import stdin
import time

start_time = time.time()


def sort_list(A):
    # NOTICE: The sorted list must be returned.
    less, equal, greater = [], [], []
    if len(A) > 1:
        pivot = A[0]
        for num in A:
            if num > pivot:
                greater.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                less.append(num)
        return sort_list(less) + equal + sort_list(greater)
    else:
        return A


def find(A, lower, upper):
    if lower < A[0]:
        lower = A[0]
    else:
        lower = find_lower(A, lower)
    if upper > A[-1]:
        upper = A[-1]
    else:
        upper = find_upper(A, upper)
    result = []
    result.append(lower)
    result.append(upper)
    return result


def find_lower(A, num):
    if len(A) == 0:
        return False
    elif len(A) == 1:
        return A[0]
    else:
        midpoint = len(A) // 2
        if A[midpoint] == num:
            return A[midpoint]
        else:
            if num > A[midpoint - 1] and num < A[midpoint]:
                return A[midpoint - 1]
            elif len(A) == 1:
                return A[0]
            elif num < A[midpoint]:
                return find_lower(A[:midpoint], num)
            elif num > A[midpoint]:
                return find_lower(A[midpoint:], num)


def find_upper(A, num):
    if len(A) == 0:
        return False
    elif len(A) == 1:
        return A[0]
    else:
        midpoint = len(A) // 2
        if A[midpoint] == num:
            return A[midpoint]
        else:
            if num < A[midpoint] and num > A[midpoint - 1]:
                return A[midpoint]
            elif len(A) == 1:
                return A[0]
            elif num < A[midpoint]:
                return find_upper(A[:midpoint], num)
            elif num > A[midpoint]:
                return find_upper(A[midpoint:], num)


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
    sorted_list = sort_list(input_list)
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
