def trap(height):
    """
    Two Pointers

    Intuition
        By using two pointers, we leverage the idea that water trapped is determined by the shorter boundary. We move the pointer of the shorter boundary inward, updating the maximum heights and water calculations dynamically.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
                print(total_water, left, "left")
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
                print(total_water, right, "right")
            right -= 1

    return total_water

    """
    Brute Force Solution

    Intuition
        The brute force solution involves iterating over each bar and calculating the amount of water that can be trapped above it. To determine the trapped water above a bar, you find the maximum height to the left and the maximum height to the right. The water above the current bar will be the minimum of these two maximum heights minus the height of the current bar.

        For each position in the array, the water that can be trapped is determined by the maximum boundary heights on both sides. By traversing each bar and calculating the left and right maximum heights, we determine the potential water trapped at that position.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    total_water = 0
    n = len(height)

    for i in range(n):
        # Find the maximum height on the left up to the current point
        max_left = max(height[:i+1])

        # Find the maximum height on the right from the current point
        max_right = max(height[i:])

        # Calculate the trapped water above the current bar
        water_at_i = min(max_left, max_right) - height[i]

        total_water += water_at_i

    return total_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = trap(height)
print(ans)  # Output: 6