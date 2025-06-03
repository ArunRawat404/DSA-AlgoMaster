def convert(s, numRows):
    """
    Simulate Zigzag Pattern

    Intuition:
        The basic idea is to simulate the process of writing characters in a zigzag pattern row by row. We move downwards to fill each row and once we hit the bottom row, we change direction to move upwards diagonally.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if numRows == 1 or numRows >= len(s):
        return s

    # List of strings, each represents a row in the zigzag pattern.
    rows = [''] * numRows

    current_row = 0
    # flag to indicate the current direction (up or down)
    step = 1

    for char in s:
        # Add the character to the current row
        rows[current_row] += char

        # Decide whether we need to move up or down
        if current_row == 0:
            step = 1
        elif current_row == numRows - 1:
            step = -1

        # Move to the next row
        current_row += step

    # Concatenate all rows to get the final converted string
    return ''.join(rows)


    """
    Using Cycle Calculation

    Intuition:
        Instead of simulating each row and direction change, we can leverage the repeating pattern in the zigzag format. Characters can be grouped by cycle sections for more efficient construction.

        Determine the cycle length, which is the period after which the pattern repeats (2 * numRows - 2).
        For each row, pick characters located at indices that contribute to this row within each cycle.
        Collect and concatenate these characters directly for the result.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if numRows == 1 or numRows >= len(s):
        return s
    
    result = ""
    cycle_len = 2 * (numRows - 1)

    for r in range(numRows):
        # Traverse through the given string to get characters belonging to this row
        for char in range(r, len(s), cycle_len):
            # Add the primary character in each cycle
            result += s[char]

            # If it's not the first or last row, add the diagonal character
            if r != 0 and r != numRows - 1 and char + cycle_len - 2 * r < len(s):
                result += s[char + cycle_len - 2 * r]

    return result

s = "PAYPALISHIRING"
numRows = 4
answer = convert(s, numRows)
print(answer)  # Output: 'PINALSIGYAHRPI'