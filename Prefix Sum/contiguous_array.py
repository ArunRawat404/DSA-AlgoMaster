def findMaxLength(nums):
    """
    Prefix Sum with HashMap

    Intuition
        The key observation here is to use a prefix sum strategy combined with a hashmap for efficient lookup:
            Convert the problem of finding equal numbers of 0's and 1's to finding subarrays whose elements sum to zero if we use a modified counting scheme (e.g., treat 0 as -1).
            Track cumulative sums and use a hashmap to quickly find if a particular cumulative sum has been seen before, which would indicate a subarray with zero sum.

        For every element, we increment or decrement the cumulative sum. If the same sum has been seen before, it means the subarray elements between the two instances of this sum have balanced 0's and 1's.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    sum_index_map = {0: -1}
    max_length = 0
    cumulative_sum = 0

    for i, num in enumerate(nums):
        # Adjust cumulative sum, treat 0 as -1
        if num == 0:
            cumulative_sum -= 1
        else:
            cumulative_sum += 1
        
        # Check if this cumulative sum has been seen before
        if cumulative_sum in sum_index_map:
            # The subarray between the first occurrence and now has equal 0’s and 1’s
            max_length = max(max_length, i - sum_index_map[cumulative_sum])
        else:
            # Store the first occurrence of this sum
            sum_index_map[cumulative_sum] = i
    
    return max_length

nums = [0,1,1,1,1,1,0,0,0]
ans = findMaxLength(nums)
print(ans)  # Output: 6