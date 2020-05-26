from sys import stdin


def min_coins_greedy(coins, value):
    x = 0
    used = 0
    while value > 0:
        if coins[x] <= value:
            mult = int(value / coins[x])
            value -= coins[x] * mult
            used += mult
        else:
            x += 1
    return used


def min_coins_dynamic(coins, value):

    # We initialize a table with coin 1 since all examples have coin with value 1
    table = list(range(0, value + 1))

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin

    # Making the coin column
    for coin in coins:
        # making rows for the columns
        if coin > value:
            continue
        # Iterate over the same array over and over again
        for j in range(coin, value + 1):
            if table[j - coin] + 1 < table[j]:
                table[j] = table[j - coin] + 1
    return table[value]


# go through all coins and see if they have modulo the coin before
def can_use_greedy(coins):
    for i in range(len(coins) - 1):
        if coins[i] % coins[i + 1] != 0:
            return False
    return True


coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if can_use_greedy(coins):
    for line in stdin:

        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))
