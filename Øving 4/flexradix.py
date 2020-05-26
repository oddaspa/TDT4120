#!/usr/bin/python3

from sys import stdin



def flexradix(A, d):
    # Returns the list A sorted.

    # creates a new list of the words sorted after length
    list3 = sort_length(A)
    return counting_sort(list3, d)


def counting_sort(A, d):
    # creates empty list of length of the longest word
    list = [0] * d
    # appends the length of a word to the list
    for word in A:
        list[len(word) - 1] = list[len(word) - 1] + 1
    # appends the number of words
    for i in range(d - 1, 0, -1):
        list[i - 1] = list[i - 1] + list[i]

    for i in range(d, -1, -1):
        F = A[len(A) - list[i - 1] :]
        B = [0] * len(F)
        C = [0] * 26
        for j in range(len(F)):

            index = ord(F[j][i - 1]) - 97

            C[index] = C[index] + 1
        for j in range(1, 26):
            C[j] = C[j] + C[j - 1]
        for j in range(len(F) - 1, -1, -1):

            index = ord(F[j][i - 1]) - 97
            B[C[index] - 1] = F[j]
            C[index] = C[index] - 1

        A[len(A) - list[i - 1] :] = B
    return A


def sort_length(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if len(A[i]) > len(A[j]):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()
