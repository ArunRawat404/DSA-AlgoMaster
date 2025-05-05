def majority_element(nums):
    """
    Boyer-Moore Voting Algorithm
        This algorithm finds the majority element by maintaining a count, incrementing for the same element, and decrementing for different elements.

    Intuition
        The algorithm uses the fact that a majority element appears more than half the time in the list, allowing us to "vote" and cancel out non-majority elements.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

    """
    Hash Map Counting
        Using a dictionary to count occurrences of each element in the list and verifying which element is the majority by comparing it to n/2.

    Intuition
        This approach leverages the use of a hash map to store counts, allowing for constant time complexity checks for the count of each element.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

#     counts = {}
#
#     majority_count = len(nums) // 2
#
#     for num in nums:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1
#         if counts[num] > majority_count:
#             return num

nums = [3, 2, 3]
answer = majority_element(nums)
print(answer)  # Output: 3
