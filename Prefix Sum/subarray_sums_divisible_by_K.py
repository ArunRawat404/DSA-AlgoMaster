def subarraysDivByK(nums, k):
    """
    Prefix Sum with Modulo Count

    Intuition
        Instead of recalculating the sum for every subarray, we utilize prefix sums. The key observation is that if two subarrays have the same modulo when divided by K, then the sum of the elements between these two subarrays is divisible by K. To achieve this, we maintain a running total of the prefix sums and use a dictionary to keep track of how many times each modulo value has appeared.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    prefix_sum = 0
    count = 0
    modulo_count = {0: 1} 
    
    for num in nums:
        prefix_sum += num  # Update the prefix sum with the current number

        # Calculate modulo to find the equivalent position in circular array formed by K
        modulo = (prefix_sum % k + k) % k  # Adjust for negative numbers for correct modulo

        if modulo in modulo_count:
            count += modulo_count[modulo]
        
        modulo_count[modulo] = modulo_count.get(modulo, 0) + 1

    return count

nums = [4,5,0,-2,-3,1]
k = 5
ans = subarraysDivByK(nums, k)
print(ans)  # Output: 7