def isIsomorphic(s, t):
    """
    Single Hash Map with Character Encoding
    
    Intuition: 
        This approach is based on encoding the characters' first occurrence in their respective strings and comparing these encoded representations. The idea is to use one hash map to assign unique identifiers (or indices) to characters based on their order of appearance.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def encode(string):
        mapping = {}
        encoded_string = []  # list of indices corresponding to each character

        for index, char in enumerate(string):
            if char not in mapping:
                mapping[char] = index  # assign the index of first occurrence
            encoded_string.append(mapping[char]) 

        return encoded_string
    
    return encode(s) == encode(t)


    """
    Mapping
    
    Intuition: 
        The idea behind this approach is to manually map each character from the first string s to the second string t and vice versa. We iterate over the strings, and for each character, we verify whether it has previously been mapped to a different character.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    s_dict = {}
    t_dict = {}
    
    for i in range(len(s)):
        # Check if mappings are not consistent
        if (s[i] in s_dict and s_dict[s[i]] != t[i]) or (t[i] in t_dict and t_dict[t[i]] != s[i]):
            return False

        # Create mappings
        s_dict[s[i]] = t[i]
        t_dict[t[i]] = s[i]

    return True

s = "paper"
t = "title"
ans = isIsomorphic(s, t)
print(ans)  # Output: False