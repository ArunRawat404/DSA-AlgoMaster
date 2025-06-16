def subarraySum(nums, k):
    """
    Cumulative Sum with HashMap

    Intuition
        This approach involves using a hash map to store cumulative sums and their frequencies. The idea is to calculate the cumulative sum as we iterate through the array. For each element, we check if there is a previous cumulative sum so that current cumulative sum minus this sum equals k. If such a sum exists, it means there is a subarray ending at the current index with sum k.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    sum_freq = {0: 1}  # Base case for a cumulative sum that directly equals k
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num
        diff = curr_sum - k
        
        # If the difference exists in the dictionary, it means there are some subarrays that sum up to k ending at the current index
        if diff in sum_freq:
            count += sum_freq[diff]
        
        # Record the current sum in the dictionary, incrementing its frequency
        if curr_sum in sum_freq:
            sum_freq[curr_sum] += 1
        else:
            sum_freq[curr_sum] = 1

    return count

nums = [1,2,3]
k = 3
ans = subarraySum(nums, k)
print(ans)  # Output: 2