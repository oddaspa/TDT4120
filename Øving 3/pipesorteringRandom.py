#!/usr/bin/python3
from sys import stdin
from random import randint
import time
start_time = time.time()


def quicksort(alist, start, end):
    #This function calls the partition and then recurse itself using the index returned by partition
    if start < end:
        pIndex = partition(alist, start, end)
        quicksort(alist, start, pIndex - 1)
        quicksort(alist, pIndex + 1, end)

    return alist


def partition(alist, start, end):
    #This function will devide the list in two halves wrt pivot
    #This will return the index of pivot after deviding
    pivot = randint(start, end)
    temp = alist[end]
    alist[end] = alist[pivot]
    alist[pivot] = temp
    pIndex = start

    for i in range(start, end):
        if alist[i] <= alist[end]:
            temp = alist[i]
            alist[i] = alist[pIndex]
            alist[pIndex] = temp
            pIndex += 1
    temp1 = alist[end]
    alist[end] = alist[pIndex]
    alist[pIndex] = temp1

    return pIndex



def find(A, lower, upper):
    if lower<A[0]:
        lower=A[0]
    else:
        lower = find_lower(A, lower)
    if upper>A[-1]:
        upper=A[-1]
    else:
        upper = find_upper(A,upper)
    result=[]
    result.append(lower)
    result.append(upper)
    return result

def find_lower(A, num):
    if len(A) == 0:
        return False
    elif len(A) ==1:
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
    if len(A) == 0:
        return False
    elif len(A) == 1:
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


def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
    sorted_list = quicksort(input_list,0,len(input_list)-1)
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))



if __name__ == "__main__":
    main()