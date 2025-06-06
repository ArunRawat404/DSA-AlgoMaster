def singleNumber(nums):
    """
    Using Bit Manipulation

    Intuition: 
        To find two unique numbers using bitwise operations, we can leverage XOR's properties. XOR of two same numbers is 0; thus XOR all numbers result in the XOR of the two unique numbers. The main challenge is to then split the numbers into two groups, so each group contains one of the unique numbers. We can differentiate the numbers by finding a set bit in the XOR result, which indicates the positions where the two numbers differ.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # XOR all numbers to get xor of the two unique numbers
    xor = 0
    for num in nums:
        xor = xor ^ num

    # Find a set bit in xor (this bit is set in one unique number and not in another)
    diff_bit = xor & -xor

    # Initialize the results for the two unique number
    result1 = 0
    result2 = 0

    for num in nums:
        # Checking if diff_bit bit is set in num.
        if num & diff_bit:
            result1 ^=  num
        else:
            result2 ^= num

    return [result1, result2]

    """
    Using HashMap

    Intuition: 
        We can use a hashmap to keep track of the frequency of each number. By the end of iterating through the list, any number that appears only once will have a frequency of one. This approach leverages the fact that numbers other than the two unique numbers appear twice.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    frequency = {}

    # Populate the hashmap with the frequency of each number
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Collect numbers that appear only once
    result = [key for key in frequency if frequency[key] == 1]

    return result

nums = [1,2,1,3,2,5]
ans = singleNumber(nums)
print(ans)  # Output: [3,5]