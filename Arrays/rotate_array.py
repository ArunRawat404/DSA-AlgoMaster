def rotate(nums, k):
    """
    Reverse Array

    Intuition:
        Reverse the entire array.
        Reverse the first k elements.
        Reverse the remaining n-k elements.

        Reversal of parts allows elements to "jump" to their target locations in constant time, making the array rotation efficient.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    n = len(nums)
    k %= n  # In case k is greater than n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse(0, n - 1)
    
    # Reverse the first k elements
    reverse(0, k - 1)
    
    # Reverse the remaining n-k elements
    reverse(k, n - 1)


    """
    Using Extra Array

    Intuition
        Create a new array and then place each element of the original array in its new position. We can create a new array, and then for each element at index i in the array, place it at the index (i + k) % n in the new array.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    # n = len(nums)
    # k %= n  # In case k is greater than n
    # rotated = [0] * n
    # for i in range(n):
    #     # Place each element in its new position
    #     rotated[(i + k) % n] = nums[i]
    # # Copy the rotated array back to nums
    # nums[:] = rotated

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5,6,7,1,2,3,4]