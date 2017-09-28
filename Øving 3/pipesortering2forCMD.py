#!/usr/bin/python3
from sys import stdin


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



def find(A, lower, upper):
    print("Lowerbound: "+str(lower))
    print("Upperbound: "+str(upper))
    print(A)
    if lower<A[0]:
        lower=A[0]
    else:
        lower = find_lower(A, lower)
    if upper>A[-1]:
        upper=A[-1]
    else:
        upper = find_upper(A,upper)
    result=[lower,upper]
    return result

def find_lower(A, num):
    print("Checking lowerbound!")
    # (Step 1) Let min = 0 and max = n - 1.
    min,max = 0, len(A)-1
    # (Step 2) Compute guess as the average of max and min, rounded down(so that it is an integer).
    while min<max:
        print("Max: "+ str(max)+" Min: "+str(min))
        guess = (min + max) // 2
        print("Our guess is: "+ str(guess) + " which means: " + str(A[guess]))
        # (Step 3) If array[guess] equals target, then stop.You found it! Return guess.
        if A[guess] == num:
            return num
        # (Step 4.1) If number is higher than guess and number is smaller than guess -1 return guess-1.
        # --- Logic --- If the number we are looking at is higher than our target and the number before our guess
        # is lower then we should pick the lower number because it is our threshold.
        if num < A[guess] and num > A[guess - 1]:
            print("Jumped into special case!")
            return A[guess-1]
        # (Step 4.2) If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
        if A[guess] < num:
            print(str(A[guess]) + " < " + str(num))
            min = guess + 1
            print("Therefore we pick: " + str(min) + " as our next min.")
            if A[min] > num:
                print("A[min] was bigger than num!")
                return A[min-1]
            if min == max:
                return A[guess]
        # (Step 4.3) Otherwise, the guess was too high.Set max = guess - 1. Go back to step 2.
        else:
            print(str(A[guess]) + " > " + str(num))
            max = guess - 1
            print("Therefore we pick: " + str(max) + " as our next max.")
            if min == max:
                return A[max]

def find_upper(A, num):
    print("Checking upperbound")
    # (Step 1) Let min = 0 and max = n - 1.
    min,max = 0, len(A)-1
    # (Step 2) Compute guess as the average of max and min, rounded down(so that it is an integer).
    while min<max:
        print("A[min]: " + str(A[min]))
        print("Max: "+ str(max)+" Min: "+str(min))
        guess = (min + max) // 2
        print("Our guess is: "+ str(guess) + " which means: " + str(A[guess]))
        # (Step 3) If array[guess] equals target, then stop.You found it! Return guess.
        if A[guess] == num:
            return num
        # (Step 4.1) If
        if num < A[guess] and num > A[guess - 1]:
            print("Jumped into special case!")
            return A[guess]
        # (Step 4.2) If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
        if A[guess] < num:
            print(str(A[guess]) + " < " + str(num))
            min = guess + 1
            print("Therefore we pick: " + str(min) + " as our next min.")
            if min == max:
                return A[min]
        # (Step 4.3) Otherwise, the guess was too high.Set max = guess - 1. Go back to step 2.
        else:
            print(str(A[guess]) + " > " + str(num))
            max = guess - 1
            print("Therefor we pick: " + str(max) + " as our next max.")
            if min == max:
                return A[max]


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