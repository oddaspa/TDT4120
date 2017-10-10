# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity

# Used in theory part of TDT4120

def knap_sack(max_weight, weight_array, value_array, n):
    # build
    K = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]
    # Bottom up approach
    for i in range(n + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight_array[i - 1] <= w:
                K[i][w] = max(value_array[i - 1] + K[i - 1][w - weight_array[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]


    return K[n][max_weight]


# Values from assignment
value_array = [18, 27, 51, 36, 24, 22, 29, 10, 24, 40]
weight_array = [320, 301, 371, 296, 303, 359, 148, 275, 296, 395]
max_weight = 740
n = len(value_array)
print("Max value is: " + str(knap_sack(max_weight, weight_array, value_array, n)) )
# 2 b)
# W = 740
# v1 = 18, v2 = 27,v3 = 51, v4 = 36, v5 = 24, v6 = 22, v7 = 29, v8 = 10, v9 = 24, v10 = 40
# w1 = 320, w2 = 301, w3 = 371, w4 = 296, w5 = 303, w6 = 359, w7 = 148, w8 = 275, w9 = 296, w10 = 395
