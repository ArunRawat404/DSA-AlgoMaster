def groupAnagrams(strs):
    """
    Using Counting and Hash Map

    Intuition: 
        Instead of sorting, we can count the frequency of each character in the string. Anagrams will have the same character frequency for all characters from 'a' to 'z'.

    Time Complexity: O(n * m), where m is the length of the string
    Space Complexity: O(n * m)
    """

    anagrams = {}

    for s in strs:
        # Create a count of 26 zeros (one for each letter)
        count = [0] * 26
        
        # Count the occurrences of each character
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Convert the list to a tuple so it can be a dictionary key
        count_tuple = tuple(count)

        # Append the original string to the correct group in the dictionary
        if count_tuple not in anagrams:
            anagrams[count_tuple] = []

        anagrams[count_tuple].append(s)

    return list(anagrams.values())

    """
    Using Sorting and Hash Map

    Intuition: 
        The idea is to use the fact that all anagrams, when sorted, result in the same string. Thus, by sorting each string in the input list and using the sorted string as the key in a hash map, we can group all anagrams together.

    Time Complexity: O(n * mlogm), where m is the length of the string
    Space Complexity: O(n * m)
    """

    anagrams = {}

    for s in strs:
        # Sort the string and use it as a hashable key3
        sorted_str = tuple(sorted(s))

        # Append the original string to the correct group in the dictionary
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []

        anagrams[sorted_str].append(s)
    
    return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
answer = groupAnagrams(strs)
print(answer)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]