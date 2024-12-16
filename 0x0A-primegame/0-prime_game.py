#!/usr/bin/python3
"""
Prime Game: Determines the winner of a game based on strategic removal
of prime numbers and their multiples. The game alternates turns
between Maria and Ben. The winner is the player who forces their
opponent into a position where they cannot make a move.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Parameters:
    x (int): Number of rounds to be played.
    nums (list): List of integers where each integer
    represents the largest
                 number in the set for that round.

    Returns:
    str: Name of the player with the most wins ("Maria" or "Ben").
         Returns None if there is a tie or invalid input.
    """
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(n):
        """
        Generates a list of all prime numbers up to a given number n.

        Parameters:
        n (int): The upper limit for generating prime numbers.

        Returns:
        list: A list of all prime numbers up to and including n.
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    # Get the maximum number from nums to precompute primes up to that limit
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Precompute sets of primes for each number in nums
    prime_sets = {}
    for num in nums:
        prime_sets[num] = set(p for p in primes if p <= num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        """
        Simulate each round of the game. Maria starts first
        and players alternate.
        Current primes represent the remaining valid numbers. A player loses
        if no primes are left to choose.
        """
        current_primes = prime_sets.get(n, set()).copy()
        if not current_primes:  # If no primes exist for this round, Ben wins
            ben_wins += 1
            continue

        turn = 0  # Maria starts first (turn 0)

        while current_primes:
            if not current_primes:  # Safeguard against empty sets
                break
            prime = min(current_primes)  # Pick the smallest remaining prime
            # Remove the prime and its multiples from the set
            current_primes -= set(range(prime, n + 1, prime))
            turn += 1

        # Maria wins if turns are odd, Ben wins if turns are even
        if turn % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner based on total wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
