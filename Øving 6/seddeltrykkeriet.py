#!/usr/bin/python3

from sys import stdin


def max_value(widths, heights, values, paper_width, paper_height):
    # we can save our values in a dictionary with size as key and value as value
    bills = {}
    smallest_bill = [min(widths), min(heights)]
    # boundry checking
    if paper_width <= 0 or paper_height <= 0:
        return 0
    # we then iterate through the input list and append the values to the keys
    for i in range(len(widths)):
        # we want to compare all lengths both horizontally and vertically
        # then we clean out the sizes that are equal. That is 3x2 = 2x3
        if heights[i] < widths[i]:
            width = heights[i]
            height = widths[i]
        else:
            width = widths[i]
            height = heights[i]

        # we want to override the value of a certain size if the value is greater than the current
        try:
            if bills[width, height] < values[i]:
                bills[width, height] = values[i]
                bills[height, width] = values[i]
        except:
            bills[width, height] = values[i]
            bills[height, width] = values[i]

    # error check in for area size
    bills = dict(
        ((key1, key2), value)
        for (key1, key2), value in bills.items()
        if key1 * key2 <= paper_height * paper_width
    )
    if bills == {}:
        return 0

    # Go through all possible solutions bottom up
    res = {}
    for w in range(paper_width + 1):
        for h in range(paper_height + 1):
            if (w, h) in bills:
                best = bills[w, h]
                if best == 0:
                    continue
            else:
                best = 0
            for cutWidth in range(1, w):
                b1 = 0
                b2 = 0
                if (cutWidth, h) in bills:
                    b1 = bills[cutWidth, h]
                if (w - cutWidth, h) in bills:
                    b2 = bills[w - cutWidth, h]
                if best < b1 + b2:
                    best = b1 + b2
            for cutHeight in range(1, h):
                b3 = 0
                b4 = 0
                if (w, cutHeight) in bills:
                    b3 = bills[w, cutHeight]
                if (w, h - cutHeight) in bills:
                    b4 = bills[w, h - cutHeight]
                if best < b3 + b4:
                    best = b3 + b4
                bills[w, h] = best
    return bills[paper_width, paper_height]


def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(":", 1)
        dim = dim_value[0].split("x", 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split("x", 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()
