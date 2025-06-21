from collections import Counter

def checkInclusion(s1, s2):
    """
    Sliding Window with HashMap

    Intuition
        This approach checks whether any permutation of s1 exists as a substring in s2.
        It uses a sliding window of length equal to s1 and a hash map (Counter) to keep
        track of character frequencies in the current window of s2.
        By comparing the character count of the window with the character count of s1,
        we can efficiently determine whether the window contains a valid permutation.

    Time Complexity: O(n)
    Space Complexity: O(1), as the space used by the Counter is constant relative to the fixed character set (assuming only lowercase letters).
    """

    s1_count = Counter(s1)
    s2_count = Counter()

    for i in range(len(s2)):
        s2_count[s2[i]] += 1
        
        if i >= len(s1):
            left_char = s2[i - len(s1)]
            if s2_count[left_char] == 1:
                del s2_count[left_char]
            else:
                s2_count[left_char] -= 1

        if s1_count == s2_count:
            return True

    return False

s1 = "ab"
s2 = "eidbaooo"
ans = checkInclusion(s1, s2)
print(ans)  # Output: True