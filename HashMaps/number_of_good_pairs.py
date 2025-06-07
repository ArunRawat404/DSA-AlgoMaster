def numIdenticalPairs(nums):
    """
    Using a Dictionary
    
    Intuition: 
        Use a dictionary to track the occurrence of each element.
        For each new occurrence of an element, update the number of good pairs because each new occurrence of an element can form a new good pair with all previous instances of that element.

    Time Complexity: O(n)
    Space Complexity: O(n),
    """

    num_freq = {}
    answer = 0

    for num in nums:
        answer += num_freq.get(num, 0)

        num_freq[num] = num_freq.get(num, 0) + 1
    
    return answer

nums = [1,2,3,1,1,3]
ans = numIdenticalPairs(nums)
print(ans)  # Output: 4