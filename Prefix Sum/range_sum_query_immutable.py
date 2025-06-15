class NumArray:
    """
    Prefix Sum Approach
    
    Intuition: 
        To optimize the sum calculation, we can use a prefix sum array. The prefix sum at each index k stores the sum of numbers from the start up to k. This allows us to calculate the sum for any range in constant time by subtracting the prefix sum values.
        By using the prefix sum approach, we significantly optimize repeated queries for sum ranges, which makes it suitable for scenarios where multiple queries are required on a large data set.

    Time Complexity: 
        Constructor: O(n), where n is the length of the array due to prefix sums calculation.
        sumRange: O(1) per query.

    Space Complexity: O(n)
    """

    def __init__(self, nums: List[int]):
        # Calculate the prefix sums
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]