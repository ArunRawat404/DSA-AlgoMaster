def zeroFilledSubarray(nums):
    """
    Optimized Sliding Window

    Intuition:

        We check for contiguous zero segments. Once we encounter a zero, we calculate how many zero-filled subarrays it can create by looking at the current zero segment size. Every new zero extends all existing zero-filled subarrays to include itself and adds new subarrays of size 1. This can be seen as an arithmetic progression.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    count = 0  # Total count of zero-filled subarrays
    zeroSeqLength = 0  # Length of the current sequence of zeros
    
    for num in nums:
        if num == 0:
            # Increment the zero sequence length
            zeroSeqLength += 1
            # Add the current sequence length to overall count
            count += zeroSeqLength
        else:
            # Reset the zero sequence length for a non-zero number
            zeroSeqLength = 0
    
    return count

nums = [0,0,0,2,0,0]
ans = zeroFilledSubarray(nums)
print(ans)  # Output: 9