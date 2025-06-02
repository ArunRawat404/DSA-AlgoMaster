def longestCommonPrefix(strs):
    """
    Approach 1: Vertical Scanning

    Intuition: 
        In this approach, we check if the character at each position in all strings is the same.

        Compare the characters one by one vertically down the rows.
        Stop when a mismatch is found or when any string's end is reached.

    Time Complexity: O(S), where S is the sum of all characters in all strings.
    Space Complexity: O(1)
    """

    for i in range(len(strs[0])):
        char = strs[0][i]
        
        for s in strs[1:]:
            # If the current string length is less than i or characters mismatch
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    return strs[0]


    """
    Approach 2: Horizontal Scanning

    Intuition: 
        The idea behind horizontal scanning is to look at the prefix common to the first two strings and then continue with this "common prefix" and the next string, and so on.

        Start by considering the entire first string as the initial common prefix.
        Compare this prefix with the next string, and adjust the length of the prefix if necessary.
        Repeat the process for all strings in the array.

    Time Complexity: O(S), where S is the sum of all characters in all strings.
    Space Complexity: O(1)
    """

    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

strs = ["flower","flow","flight"]
answer = longestCommonPrefix(strs)
print(answer)  # Output: "fl"