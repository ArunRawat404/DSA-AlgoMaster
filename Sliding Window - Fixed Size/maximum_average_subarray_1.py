def findMaxAverage(nums, k):
    """
    Sliding Window Approach

    Intuition
        The sliding window technique helps optimize the problem by maintaining a window of size k that slides through the array. By adding the next element in the array and removing the first element of the current window, you compute the sum for the next window in constant time. This reduces repeated computations of sums from overlapping subarrays, thereby enhancing efficiency.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # Calculate the initial sum of the first subarray of length k
    curr_sum = sum(nums[:k])

    n = len(nums)
    max_sum = curr_sum

    # Slide the window over the array from the (k + 1)th element to the end
    for i in range(k, n):
        # Update the sum by adding the new element and removing the oldest element
        curr_sum += nums[i] - nums[i - k]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
ans = findMaxAverage(nums, k)
print(ans)  # Output: 12.75