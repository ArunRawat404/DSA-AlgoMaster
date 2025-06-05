def singleNumber(nums):
    """
    Using Bitmasking

    Intuition:
        We use two variables, `ones` and `twos`, to track the numbers that have appeared exactly once and exactly thrice, respectively.

        For each number in the array:
        - Update `ones`: add the new bits to it, unless those bits are already in `twos`.
        - Update `twos`: add the new bits to it, unless those bits are already in `ones`.
        - At the end, `ones` contains the bits of the number that appeared exactly once.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    ones = 0
    twos = 0

    for num in nums:
        # First update `ones`, ignore bits already in `twos`
        ones = (ones ^ num) & ~twos
        # Then update `twos`, ignore bits now in `ones`1
        twos = (twos ^ num) & ~ones

    # Only the unique number remain in `ones`
    return ones

    """
    Using Bitwise Counting

    Intuition: 
        For each bit position (0 to 31), count how many numbers have that bit set.
        Since every number except one appears 3 times, all bit counts should be divisible by 3 — except for the unique number's bits.
        Use bitwise OR to construct the result from bits where count % 3 != 0.

    Time Complexity: O(32 * n)
    Space Complexity: O(1)
    """

    ans = 0
    # Loop through all 32 bits (assuming 32-bit integers)
    for i in range(32):
        bit_sum = 0

        # Count number of 1s at the i-th bit position
        for num in nums:
            if (num >> i) & 1 == 1:
                bit_sum += 1

        # Only bits that don't appear 3 times belong to the unique number
        bit_sum %= 3

        # Add that bit to the answer
        if (bit_sum):
            ans |= bit_sum << i

    # Handle negative numbers
    if ans >= 2**31:
        ans -= 2**32

    return ans

nums = [0,1,0,1,0,1,99]
ans = singleNumber(nums)
print(ans)  # Output: 99