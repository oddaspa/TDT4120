#!/usr/bin/python3
from sys import stdin
import pipesortering
import pipesorteringRandom
import time


def main():
    i = 0
    j = 0
    test_file = open("input.txt")
    input_list = []
    for x in test_file.readline().split():
        input_list.append(int(x))

    start_time1 = time.time()
    sorted_list = pipesortering.sort_list(input_list)
    checkPoint1 = time.time() - start_time1

    start_time2 = time.time()
    sorted_list2 = pipesorteringRandom.quicksort(input_list, 0, len(input_list) - 1)
    checkPoint2 = time.time() - start_time2
    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        start_time3 = time.time()
        result = pipesortering.find(sorted_list, minimum, maximum)
        checkPoint3 = time.time() - start_time3

        start_time4 = time.time()
        result2 = pipesorteringRandom.find(sorted_list2, minimum, maximum)
        checkPoint4 = time.time() - start_time4

        if result != result2:
            i += 1
            print("Lowerbound:   Upperbound:")
            print(str(minimum) + " " + str(maximum))
            print("Error:")
            print(sorted_list)
            print("Right result: " + str(result) + "...")
            print("...but got: " + str(result2))
        else:
            j += 1
    ratio = float(i) / j
    ratio1 = float("{0:.3f}".format(ratio * 100))
    print(str(ratio1) + "% feil.")
    print(
        "alg1: "
        + str(checkPoint1 + checkPoint3)
        + "ms. alg2: "
        + str(checkPoint2 + checkPoint4)
        + "ms."
    )


if __name__ == "__main__":
    main()
