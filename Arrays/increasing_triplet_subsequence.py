def increasingTriplet(nums):
    """
    Optimized Linear Scan Using Auxiliary Variables

    Intuition:
        The goal is to find a subsequence of three increasing numbers in linear time. One path is to utilize two variables to track the smallest and second smallest numbers encountered so far as we iterate through the list. When we find a number greater than our second smallest, we've found our increasing triplet.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    first_value = float('inf')
    second_value = float('inf')

    for num in nums:
        if num <= first_value:
            # Update the smallest number seen so far
            first_value = num

        elif num <= second_value:
            # Update the second smallest number that is greater than 'first'
            second_value = num

        else:
            # We have found a number greater than both first and second
            return True      
        
    return False

nums = [2,1,5,0,4,6]
answer = increasingTriplet(nums)
print(answer)  # Output: True
