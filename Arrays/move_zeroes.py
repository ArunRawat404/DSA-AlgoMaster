def move_zeroes(nums):
    """
    Two Pointer Technique

    Intuition:

        This approach improves upon the naive approach by eliminating the need for an auxiliary list. Instead, we rearrange the elements in-place using a two-pointer technique. We maintain one pointer, last_non_zero_index, to track the position of the last non-zero element. As we iterate, we swap non-zero elements with the position pointed by last_non_zero_index.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    last_non_zero_index = 0
    
    for i in range(len(nums)):
        if (nums[i] != 0):
            nums[i], nums[last_non_zero_index] = nums[last_non_zero_index], nums[i]
            last_non_zero_index += 1
        
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

