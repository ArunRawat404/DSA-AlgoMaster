def move_zeroes(nums):
    last_non_zero_index = 0
    
    for i in range(len(nums)):
        if (nums[i] != 0):
            nums[i], nums[last_non_zero_index] = nums[last_non_zero_index], nums[i]
            last_non_zero_index += 1
        
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

