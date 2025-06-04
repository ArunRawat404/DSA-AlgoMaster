def hammingWeight(n):
    """
    Brian Kernighan's Algorithm

    Intuition:
        Brian Kernighan's Algorithm is more efficient as it reduces the number of iterations in counting the number of 1 bits. The core idea is to repeatedly turn off the rightmost bit that is 1. This is done by performing n = n & (n - 1) which removes the lowest set bit.

    Time Complexity: O(k), where k is the number of 1 bits; in the worst case, it is O(32) = O(1) for a 32-bit integer.
    Space Complexity: O(1)
    """

    count = 0
    while n:
        # Turn off the rightmost/lowest set bit
        n = n & (n - 1)  
        # Increment count as a 1-bit is removed
        count += 1
    return count

    """
    Loop and Bit Shift

    Intuition:
        To count the number of 1 bits in an integer, we can repeatedly check the least significant bit (LSB) and then shift the bits of the number to the right. The bitwise AND operation with 1 helps to isolate the LSB: n & 1 will be 1 if the LSB is 1 and 0 otherwise. By right shifting the number by 1 at each step and checking the LSB, we can count all the 1 bits.
    
    Time Complexity: O(32) = O(1), since we are guaranteed a 32-bit integer.
    Space Complexity: O(1), as we only use a constant amount of space.
    """

    count = 0
    while n:
        # If the last bit is 1, increment the count
        if n & 1 == 1:
            count += 1
        # Shift bits of n right by 1
        n = n >> 1
    return count

n = 2147483645
ans = hammingWeight(n)
print(ans)  # Output: 30