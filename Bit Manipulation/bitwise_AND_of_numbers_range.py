def rangeBitwiseAnd(left, right):
    """
    Bit Manipulation Reduction

    Intuition:
        The bitwise AND (&) of a range will only keep the bits that are 1 in all numbers in that range.
        As soon as a bit flips anywhere in the range, that bit position becomes 0 in the final answer.

    Time Complexity: O(log n), as we are shifting bits right until left and right are aligned
    Space Complexity: O(1)
    """

    # Reduce the range by repeatedly zeroing out the least significant bit of right 
    while left < right:
        # Remove the least significant 1-bit from right
        right = right & (right - 1)
    return right

    """
    Shift Right

    Intuition:
        When we bitwise AND a range like [m, m+1, ..., n], only the leftmost common bits will survive. Any bits that change between m and n will become 0 in the final result.

    Time Complexity: O(log n), as we are right-shifting the numbers, which cuts their size roughly in half each time. So at most, we'll do about log₂(n) shifts.
    Space Complexity: O(1)
    """

    # Initialize a counter for shifted bits
    shift = 0
    # Shift both numbers right until they are the same
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    
    # Shift back to the original positions
    return left << shift


left = 5
right = 7
ans = rangeBitwiseAnd(left, right)
print(ans)  # Output: 4