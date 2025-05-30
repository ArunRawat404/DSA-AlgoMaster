def removeDuplicates(nums):
    """
    Two Pointer Technique
    
    Intuition:
        Pointer i: traverses each element in the array.
        Pointer j: keeps track of where the next unique element should be placed.
    
        The idea is to iterate over the array with i, and whenever a new unique element is found (i.e., nums[i] != nums[j]), we increment j and update nums[j] with nums[i]. This effectively shifts unique elements towards the beginning of the array one by one.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if not nums:
        return 0

    j = 0  

    for i in range(1, len(nums)):
        if nums[i] != nums[j]:  # If a unique element is found
            j += 1
            nums[j] = nums[i]  # Set the unique element at index j

    return j + 1

nums = [0,0,1,1,1,2,2,3,3,4]
ans = removeDuplicates(nums)
print(ans)  # Output: 5