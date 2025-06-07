def maxNumberOfBalloons(text):
    """
    Frequency Count
    
    Intuition: 
        The task is to determine how many times the word "balloon" can be formed using the letters in a given string text. The word "balloon" consists of b, a, l, l, o, o, n. We need to track the frequency of these letters and ensure we have enough to form the word in entirety.

    Time Complexity: O(n)
    Space Complexity: O(1), since we are using a fixed size dictionary for a constant set of characters.
    """

    text_freq = {}
    for char in text:
        text_freq[char] = text_freq.get(char, 0) + 1
    
    balloon_freq = {}
    for char in 'balloon':
        balloon_freq[char] = balloon_freq.get(char, 0) + 1
    
    res = float('inf')
    for char in 'balloon':
        res = min(res, text_freq.get(char, 0) // balloon_freq[char])

    return res

text = "loonbalxballpoon"
ans = maxNumberOfBalloons(text)
print(ans)  # Output: 2