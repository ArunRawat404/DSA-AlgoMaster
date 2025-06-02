def isPalindrome(s):
    """
    Two Pointer Approach

    Intuition: 
        We can use two pointers directly on the original string, skipping non-alphanumeric characters and comparing characters in lower case as we go.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    start = 0
    end = len(s) - 1

    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        else:
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
    
    return True

s = "A man, a plan, a canal: Panama"
answer = isPalindrome(s)
print(answer)  # Output: True