def threeSum(nums):
    """
    Sorting and Two-Pointer Technique

    Intuition
        A efficient way is to sort the array and use the two-pointer technique. The idea is to fix one number and find the other two numbers using two pointers to minimize the sum calculation efficiently.

    Time Complexity: O(n^2)
    Space Complexity: O(m), where m is the number of unique triplets that sum to zero
    """

    nums.sort()
    triplets = []  

    for i in range(len(nums) - 2):
        # Skip the same element to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            print(i, "i")
            continue

        start = i + 1
        end = len(nums) - 1

        while start < end:
            # Calculate the sum of the current triplet
            current_sum = nums[i] + nums[start] + nums[end]

            if current_sum == 0:
                triplets.append([nums[i], nums[start], nums[end]])

                # Move both pointers past duplicates
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                start += 1
                end -= 1

            elif current_sum > 0:
                end -= 1
            else:
                start += 1

    return triplets

nums = [-1,0,1,2,-1,-4]
ans = threeSum(nums)
print(ans)  # Output: [[-1,-1,2],[-1,0,1]]