def merge(nums1, m, nums2, n):
    """
    In-place Merge from the End

    Intuition
        Since nums1 has enough space to accommodate the merged array, starting from the back allows us to avoid moving elements repeatedly. We can fill nums1 from the end towards the beginning, placing the larger of the two elements from nums1 and nums2 each time.

    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """

    # Pointers for nums1, nums2, and the end of the merged array
    p1, p2, end = m - 1, n - 1, m + n - 1

    # While there are elements in both nums1 and nums2 to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[end] = nums1[p1]
            p1 -= 1
        else:
            nums1[end] = nums2[p2]
            p2 -= 1
        end -= 1

    # If there are remaining elements in nums2, copy them
    while p2 >= 0:
        nums1[end] = nums2[p2]
        p2 -= 1
        end -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3,5,6]