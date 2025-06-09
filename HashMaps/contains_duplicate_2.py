def containsNearbyDuplicate(nums, k):
    """
    HashMap
    
    Intuition: 
        A hash map can be used to store the most recent index of each element previously encountered. This allows us to quickly verify if there is a duplicate within the allowed index range by checking if the stored index minus the current index is within the threshold k.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    # Dictionary for tracking last seen index of numbers
    num_index_map = {}

    for index, num in enumerate(nums):
        # Check if the number is in the map and within allowed index difference
        if num in num_index_map and index - num_index_map[num] <= k:
            return True
        
        # Update the dictionary with current index of the number
        num_index_map[num] = index

    return False

nums = [1,0,1,1]
k = 1
answer = containsNearbyDuplicate(nums, k)
print(answer)  # Output: True