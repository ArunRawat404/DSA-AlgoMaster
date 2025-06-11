from collections import Counter

def reorganizeString(s):
    """
    Count and Sort
    
    Intuition: 
        This approach relies on sorting the characters based on frequency and then attempting to interleave them in a way that no two adjacent characters are the same. 

    Time Complexity: O(n + k log k)
    Space Complexity: O(n)
    """

    char_count = Counter(s)
    
    # Sort characters by frequency
    sorted_chars = sorted(char_count, key=lambda x: -char_count[x])
    
    res = [''] * len(s)
    index = 0

    # Fill characters starting with most frequent
    for char in sorted_chars:
        count = char_count[char]
        if count > (len(s) + 1) // 2:
            return ""
        
        for _ in range(count):
            if index >= len(s):
                index = 1
            res[index] = char
            index+= 2
        
    return ''.join(res)

s = "aab"
answer = reorganizeString(s)
print(answer)  # Output: 'aba'