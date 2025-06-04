def countBits(n):
    """
    Dynamic Programming - Most Significant Bit

    Intuition:
        This optimization is based on the observation that if you know the most significant bit of a number, the rest is just like a smaller number that you have already solved for.

        Identify the most significant bit that is a power of 2.
        For a number i, its bits count is 1 + bits[i - power] where power is the largest power of 2 less than i.
        some smaller number x. The number of 1s for this combination is then 1 + countBits(x).

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    dp = [0] * (n + 1)
    offset = 1  # to track the latest power of two

    for i in range(1, n + 1):
        # update offset when we get to the next power of two
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp

    """
    Naive Approach

    Intuition:
        The simplest approach is to count the 1 bits for each number.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """

    def num_1_bits(num):
        count = 0
        while num:
            # Turn off the rightmost/lowest set bit
            num = num & (num - 1)  
            # Increment count as a 1-bit is removed
            count += 1
        return count

    answer = []
    for i in range(n + 1):
        answer.append(num_1_bits(i))

    return answer

n = 5
ans = countBits(n)
print(ans)  # Output: [0,1,1,2,1,2]