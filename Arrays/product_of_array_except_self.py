def productExceptSelf(nums):
    """
    Optimal Space Prefix and Suffix Product Approach
    
    Intuition:
        To further optimize space, we can reuse the output array for storing the prefix products, while calculating the suffix product on the fly. This eliminates the need for extra space dedicated to suffix storage.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
        
    length = len(nums)

    # Initialize the output array for prefix products and final result
    output = [1] * length

    # Calculate prefix products directly into the output array
    for i in range(1, length):
        output[i] = output[i - 1] * nums[i - 1]

    suffix_product = 1
    for j in range(length - 1, -1, -1):
        # Multiply the suffix product with the current output product
        output[j] = output[j] * suffix_product

        # Update the suffix product for the next iteration
        suffix_product = suffix_product * nums[j]

    return output

    """
    Prefix and Suffix Product Approach
    
    Intuition:
        This approach use array for prefix and suffix products. A prefix product is the product of all elements before a given index, and a suffix product is the product of all elements after a given index. We can then easily compute the desired product by multiplying the prefix and suffix products.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    length = len(nums)

    prefix = [1] * length
    suffix = [1] * length
    output = [1] * length

    # Calculate prefix products
    for i in range(1, length):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Calculate suffix products
    for i in range(length - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Calculate the result by multiplying prefix and suffix
    for i in range(length):
        output[i] = prefix[i] * suffix[i]

    return output

nums = [1,2,3,4]
ans = productExceptSelf(nums)
print(ans)  # Output: [24,12,8,6]