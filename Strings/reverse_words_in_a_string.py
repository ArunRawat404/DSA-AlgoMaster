def reverseWords(s):
    """
    Reverses the words in a string using word accumulation.

    Intuition:
        We iterate over the string character by character, accumulate characters into a word until a space is found, then prepend the word to the result string to reverse the order. A space is added at the end to capture the last word.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    word = ""
    reverse_words = ""

    #  + " " for adding last word
    for char in s + " ":
        if char != " ":
            word += char
        elif word:
            reverse_words = word + " " + reverse_words
            word = ""

    # removing the extra space at the end
    return reverse_words[:-1]

s = "the sky is blue"
answer = reverseWords(s)
print(answer)  # Output: "blue is sky the"