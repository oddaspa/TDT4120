from sys import stdin

Inf = 1000000000


def min_coins_greedy(coins, value):
    coins.sort(reverse=True)
    x = 0
    used = 0
    while value > 0:
        if coins[x] <= value:
            value -= coins[x]
            used += 1
        else:
            x+=1
    return used


def min_coins_dynamic(coins, value):

    # table[i] will be storing the minimum number of coins required
    # for i value. So table[V] will have result int table[V+1];

    # Base case (If given value V is 0)
    table = [1]
    table[0] = 0
    # Initialize all table values as Infinite
    for i in range(value):
        table.append(Inf)
    # Compute minimum coins required for all
    # values from 1 to V
    for j in range(value):
    # Go through all coins smaller than i
        for k in range(len(coins)-1):
            if (coins[k] <= j):
                sub_res = table[j-coins[k]]
                if ((sub_res != Inf) and (sub_res + 1 < table[j])):
                    table[j] = sub_res + 1
        print(table)
    return table[value]


def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    return
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))