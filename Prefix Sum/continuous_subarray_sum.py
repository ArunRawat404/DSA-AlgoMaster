def checkSubarraySum(nums, k):
    """
    Prefix Sum with HashMap

    Intuition
        To optimize, we utilize the property of modular arithmetic. If sum[i] % k == sum[j] % k for any i < j, the sum of the elements between i and j is a multiple of k. We use a hashmap to store the remainder of the prefix sum modulo k and the earliest index it was seen at. This approach ensures that we can find two such indices in linear time.

    Time Complexity: O(n)
    Space Complexity: O(min(n, k))
    """

    # Dictionary to store the first occurrence of prefix sum modulo k
    prefix_sum_mod_k = {0: -1}  # Handles case where subarray starts from index 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]
        mod = curr_sum % k
        
        # If this mod has been seen before, check the length of the subarray
        if mod in prefix_sum_mod_k:
            if i - prefix_sum_mod_k[mod] > 1:
                return True
        else:
            prefix_sum_mod_k[mod] = i

    return False

nums = [23,2,4,6,7]
k = 6
ans = checkSubarraySum(nums, k)
print(ans)  # Output: True