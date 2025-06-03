def singleNumber(nums):
    """
    Using XOR

    Intuition: 
        XOR of a ^ a = 0
        XOR of b ^ 0 = b
        So when we XOR all the elements of array nums, all the pairs will result in 0 and XOR of 0 with number which appear once is number itself.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    result = 0
    for num in nums:
        result = result ^ num

    return result

nums = [4,1,2,1,2]
ans = singleNumber(nums)
print(ans)