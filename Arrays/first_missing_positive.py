def firstMissingPositive(nums):
    """
    In-Place Hashing (Cyclic Sort)

    Intuition
        The optimal solution leverages the fact that the size of the input array determines the range of numbers we should check. A number n in an array of size n can only be from 1 to n for us to consider it as a potential minimum positive integer. Using this observation, we can rearrange the numbers in a way that each number is placed at an index corresponding to its value (i.e., 1 at index 0, 2 at index 1, etc.). This is similar to the cyclic sort pattern.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    n = len(nums)
    for i in range(n):

        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap numbers to their correct position.
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
    # If after rearrangement, nums[i] != i + 1, i + 1 is the missing number.
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all numbers are in their correct positions, the missing number is n + 1
    return n + 1

nums = [3, 4,-1,1]
answer = firstMissingPositive(nums)
print(answer)  # Output: 2