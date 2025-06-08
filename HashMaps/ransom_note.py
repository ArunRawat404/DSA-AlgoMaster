def canConstruct(ransomNote, magazine):
    """
    HashMap
    
    Intuition: 
        By counting the number of occurrences of each character in both the ransom note and the magazine, we can efficiently determine if the magazine contains enough of each character to construct the ransom note.

    Time Complexity: O(n + m)
    Space Complexity: O(n), since we are using a fixed size dictionary for a constant set of characters.
    """

    char_count = {}

    # Count frequency of each character in the magazine
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if we have enough characters for the ransom note
    for char in ransomNote:
        if char_count.get(char, 0) <= 0:
            return False
        char_count[char] -= 1

    return True

ransomNote = "aa"
magazine = "aab"
ans = canConstruct(ransomNote, magazine)
print(ans)  # Output: True

