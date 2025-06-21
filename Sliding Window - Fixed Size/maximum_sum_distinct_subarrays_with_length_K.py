def maximumSubarraySum(nums, k):
    """
    Sliding Window + Set Approach

    Intuition
        To optimize, we use a sliding window with a set to maintain the distinctness of the subarray. The sliding window helps us in managing the subarray size and the set helps in maintaining distinct elements.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """

    n = len(nums)
    curr_sum = 0
    max_sum = 0

    current_set = set()
    left = 0

    for right in range(n):
        # Check and remove duplicates
        while nums[right] in current_set:
            current_set.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
        
        # Add the current element to the window
        current_set.add(nums[right])
        curr_sum += nums[right]

        # Check if the window is of size k
        if right - left + 1 == k:
            max_sum = max(max_sum, curr_sum)

            # Slide the window forward by removing the left element
            current_set.remove(nums[left])
            curr_sum -= nums[left]
            left += 1

    return max_sum

nums = [1,5,4,2,9,9,9]
k = 3
ans = maximumSubarraySum(nums, k)
print(ans)  # Output: 15