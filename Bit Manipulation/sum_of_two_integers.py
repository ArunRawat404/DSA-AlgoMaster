def getSum(a, b):
    """
    Using Bit Manipulation
    
    Intuition: 
        The problem requires us to sum two integers without using the + or - operators. The addition operation can be decomposed into a series of bit manipulations:

        XOR (^): This operation will add two bits as if it were an addition without carrying (i.e., 0+0=0, 1+0=1, 0+1=1, 1+1=0).
        AND (&): This will identify the bits that result in a carry when adding the two numbers.
        Left shift (<<): This is used to shift the carry by one bit to align it with the original number.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    # Mask for bits beyond 32, it is same as 0b1111111111111111111111111111111
    MASK = 0xFFFFFFFF

    # This is the maximum positive value a signed 32-bit integer can hold, it is same as 0b01111111111111111111111111111111
    MAX = 0x7FFFFFFF

    # Iterating until there are no carries
    while b != 0:
        # Carry is AND, shifted left by 1
        carry = (a & b) << 1

        # Add without carry using XOR
        a = (a ^ b) & MASK

        # Apply mask to carry
        b = carry & MASK

    # If a is negative, use ~ operation with MASK
    return a if a <= MAX else ~(a ^ MASK)

a = 2
b = 3
ans = getSum(a, b)
print(ans)  # Output: 5