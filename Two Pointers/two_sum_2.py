def twoSum(numbers, target):
    """
    Two Pointers

    Intuition
        Use two pointers: one starting at the beginning of the array (left) and another at the end (right). Calculate the sum of the elements at these indices. If the sum equals the target, return the indices. If the sum is less than the target, increment the left pointer to increase the sum. If the sum is greater than the target, decrement the right pointer to decrease the sum.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    start = 0
    end = len(numbers) - 1

    while start < end:
        current_sum = numbers[start] + numbers[end]

        if current_sum == target:
            # Found the pair, return 1-based indices
            return [start + 1, end + 1]
        elif current_sum < target:
            start += 1
        else:
            end -= 1

numbers = [2,7,11,15]
target = 9
ans = twoSum(numbers, target)
print(ans)  # Output: [1, 2]