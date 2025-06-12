def longestConsecutive(nums):
    """
    Using HashSet

    Intuition
        We can use a HashSet to quickly look up the existence of a number. The idea is to iterate through the array and for each number, try to build the longest consecutive sequence that starts with this number.

        To minimize redundant work, we only start building sequences for numbers that are the start of a sequence (i.e., num - 1 is not in the set).

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start a new sequence if `num - 1` is not present
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Keep increasing the streak while consecutive numbers are found
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

    """
    Sort and Check Consecutivity

    Intuition
        The simplest approach to solve the problem is to sort the array first, which allows us to identify consecutive elements by iterating through the sorted array. When the elements are sorted, the problem of finding the longest consecutive sequence becomes one of counting the longest sequence of n, n+1, n+2, ... etc, in the sorted array.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """

    if not nums:
        return 0

    nums.sort()
    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        # If current number is equal to the previous, skip it
        if nums[i] == nums[i - 1]:
            continue
        # If they are consecutive, increase current streak
        elif nums[i] == nums[i - 1] + 1:
            current_streak += 1
        else:
            # Reset the current streak and update the max streak
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1
    
    # Update longest streak at the end of iteration
    return max(longest_streak, current_streak)

nums = [0,3,7,2,5,8,4,6,0,1]
ans = longestConsecutive(nums)
print(ans)  # Output: 9