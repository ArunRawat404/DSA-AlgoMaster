def maxArea(height):
    """
    Two Pointers

    Intuition
        The two pointers technique optimizes the solution by using the fact that the area is limited by the shorter of the two lines. By starting with two pointers at the beginning and end of the array, we can gradually move towards the center, trying to find a configuration that can provide a larger area with each step. When we move the shorter of the two lines inward, we have a chance to increase the area because we are increasing the distance between the two lines while potentially finding a taller line.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    start = 0
    end = len(height) - 1
    max_area = 0

    while start < end:
        width = end - start 
        area = min(height[start], height[end]) * width

        max_area = max(max_area, area)

        # Move the pointer of the shorter line
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
ans = maxArea(height)
print(ans)  # Output: 49