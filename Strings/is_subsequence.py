def isSubsequence(s, t):
    """
    Two Pointer Approach

    Intuition: 
        The approach is to check whether string s is a subsequence of string t by scanning through t character by character. We maintain an index that keeps track of how many characters from s we've successfully matched in order. As we iterate through t, whenever we find a character that matches the current character in s, we move the index forward. If we manage to match all characters of s before we finish scanning t, we can conclude that s is a subsequence of t. If the loop finishes and we haven't matched all characters from s, then it's not a subsequence.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # If s is empty, it is a subsequence
    if len(s) == 0:
        return True

    # if length of s is longer than t, it can't be a subsequence
    if len(s) > len(t):
        return False
    
    index = 0

    for char in t:
        # If character in t matches the character in s, move to the next character in s
        if char == s[index]:
            index += 1
        
        # If all characters in s have been matched, s is a subsequence of t
        if index >= len(s):
            return True
        
    return False

s = "acx"
t = "ahbgdc"
answer = isSubsequence(s, t)
print(answer)  # Output: False