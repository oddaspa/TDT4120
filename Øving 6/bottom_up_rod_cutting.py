# quick method for assignment in TDT4120
cutting = []


def rod_cutting(n, prices):

    if n == 1:
        return prices[0]

    max_val = 0
    for i in range(n):
        # max of our current value or price[i] + cutting the rod
        max_val, cut = max(max_val, prices[i] + rod_cutting(n - i - 1, prices)), i
        print((max_val))
        if max_val == prices[i] + rod_cutting(n - i - 1, prices):
            new_cut = cut
        cutting.append(new_cut)
    return max_val


prices = [2, 4, 5]
n = len(prices)
print("Max price: " + str(rod_cutting(n, prices)))
for x in range(n):
    whole_rod = "|" + (n) * "-" + "|"
    print("We have: " + str(whole_rod))
    print("We cut rod at " + str(cutting[x]))
    print(
        "The value of "
        + "|"
        + (cutting[x] + 1) * "-"
        + "|"
        + " is "
        + str(prices[cutting[x]])
    )
    n = n - (cutting[x] + 1)


# p1 = 4, p2 = 9, p3 = 15, p4 = 18, p5 = 21, p6 = 28, p7 = 31, p8 = 37
