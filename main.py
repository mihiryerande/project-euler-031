# Problem 31:
#     Coin Sums
#
# Description:
#     In the United Kingdom the currency is made up of pound (£) and pence (p).
#     There are eight coins in general circulation:
#         1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
#     It is possible to make £2 in the following way:
#          1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
#     How many different ways can £2 be made using any number of coins?

COINS = [1, 2, 5, 10, 20, 50, 100, 200]       # All possible coin values
NEXT_COIN = dict(zip(COINS[1:], COINS[:-1]))  # Map of each coin to next-lowest-valued coin

COIN_SUM_WAYS = dict()


def coin_sum_ways(n: int, max_coin: int) -> int:
    """
    Returns the number of ways to make `n` pence
      using any number of coins in general circulation
      where the maximum value of any individual coin is at most `max_coin`.
    Note that this also includes using zero of `max_coin`.
    
    Args:
        n        (int): Non-negative integer
        max_coin (int): Maximum value among coins summing to `n`

    Returns:
        (int): Number of ways to make `n` pence using any number of coins
                 having maximum value `max_coin`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n >= 0
    assert type(max_coin) == int and max_coin > 0

    # Idea:
    #     Attempt to use `max_coin` as much as possible to achieve `n`.
    #     Siphon off `max_coin` one-by-one, using smaller coins to fill the gap.
    #     To avoid redundant counting, maintain computed counts in `COIN_SUM_WAYS`

    global COIN_SUM_WAYS
    if (n, max_coin) in COIN_SUM_WAYS:
        # Already computed this
        return COIN_SUM_WAYS[(n, max_coin)]
    else:
        # Haven't computed this case yet
        if n == 0:
            # Only one way to satisfy vacuous case where total is zero
            ways = 1
        elif max_coin == 1:
            # Coin sum is accomplished by `n` coins of 1p
            ways = 1
        else:
            # Use as much of `max_coin` as possible
            next_coin = NEXT_COIN[max_coin]
            ways = 0
            max_coin_count_max, remaining_sum = divmod(n, max_coin)
            for _ in range(max_coin_count_max, -1, -1):
                ways += coin_sum_ways(remaining_sum, next_coin)
                remaining_sum += max_coin  # Siphon off one `max_coin`
        COIN_SUM_WAYS[(n, max_coin)] = ways
        return ways


def main(n: int) -> int:
    """
    Returns the number of ways to make `n` pence
      using any number of coins in general circulation, which are:
        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    Args:
        n (int): Natural number

    Returns:
        (int): Number of ways to make `n` pence using any number of coins

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0
    global COINS
    return coin_sum_ways(n, COINS[-1])


if __name__ == '__main__':
    total_pence = int(input('Enter a coin sum (natural number): '))
    coin_sum_counts = main(total_pence)
    print('Number of ways to make {} pence using coins:'.format(total_pence))
    print('  {}'.format(coin_sum_counts))
