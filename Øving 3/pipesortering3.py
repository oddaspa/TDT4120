#!/usr/bin/python3
from sys import stdin

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
    sorted_list = sort_list(input_list)



    for line in stdin:
        word = line.split()
        lower = int(word[0])
        upper = int(word[1])

    low = sorted_list[0]
    high = sorted_list[-1]

    if lower <= low:
        lower = low
    else:
        lower = find_lower(sorted_list, lower)
    if upper >= high:
        upper = high
    else:
        upper = find_upper(sorted_list, upper)
    print(str(lower) + " " + str(upper))


def sort_list(A):
    # NOTICE: The sorted list must be returned.
    less,equal,greater = [],[],[]
    if len(A) > 1:
        pivot = A[0]
        for num in A:
            if num > pivot:
                greater.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                less.append(num)
        return sort_list(less)+equal+sort_list(greater)
    else:
        return A

def find_lower(A, num):
    if len(A) ==1:
        return A[0]
    else:
        midpoint = len(A)//2
        if A[midpoint]==num:
            return A[midpoint]
        else:
            if num>A[midpoint-1] and num<A[midpoint]:
                return A[midpoint-1]
            elif len(A)==1:
                return A[0]
            elif num<A[midpoint]:
                return find_lower(A[:midpoint],num)
            elif num>A[midpoint]:
                return find_lower(A[midpoint:],num)

def find_upper(A, num):
    if len(A) == 1:
        return A[0]
    else:
        midpoint = len(A)//2
        if A[midpoint]==num:
            return A[midpoint]
        else:
            if num<A[midpoint] and num>A[midpoint-1]:
                return A[midpoint]
            elif len(A)==1:
                return A[0]
            elif num<A[midpoint]:
                return find_upper(A[:midpoint],num)
            elif num>A[midpoint]:
                return find_upper(A[midpoint:],num)





if __name__ == "__main__":
    main()