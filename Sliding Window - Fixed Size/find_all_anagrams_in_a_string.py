from collections import Counter

def findAnagrams(s, p):
    """
    Sliding Window with HashMap

    Intuition
        This approach uses a sliding window combined with a hash map to keep track of character counts efficiently. The goal is to eliminate the need to recompute the frequency map for each new substring.

    Time Complexity: O(n)
    Space Complexity: O(1), as the space used by the Counter is constant relative to the fixed character set (assuming only lowercase letters).
    """

    result = []

    p_count = Counter(p)
    s_count = Counter()

    for i in range(len(s)):
        s_count[s[i]] += 1

        # Remove character outside the window
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        # Compare dictionaries, add start index to results if an anagram is found
        if p_count == s_count:
            result.append(i - len(p) + 1)
            
    return result

s = "cbaebabacd"
p = "abc"
ans = findAnagrams(s, p)
print(ans)  # Output: [0, 6]