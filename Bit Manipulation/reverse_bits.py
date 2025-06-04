def reverseBits(n):
    """
    Bit Manipulation

    Intuition: 
        We need to reverse the order of these bits. We'll perform this by iterating through each bit position of the input number, from least significant to most significant, and setting them in the correct reverse position in the result number.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    result = 0
    
    for _ in range(32):
        # Extract the least significant bit of n
        bit = n & 1
        
        # Shift the extracted bit to its correct reversed position
        result = (result << 1) | bit
        
        # Prepare n for the next iteration by shifting right
        n >>= 1
    
    return result

n = 11111111111111111111111111111101
ans = reverseBits(n)
print(ans)  # Output: 3221225471