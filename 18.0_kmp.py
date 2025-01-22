def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array.
    This array is used to skip unnecessary comparisons.
    """
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    Perform KMP pattern matching.
    Returns the starting indices of all occurrences of the pattern in the text.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    indices = []  # To store the indices of matched patterns
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  # A match is found
            indices.append(i - j)
            j = lps[j - 1]  # Reset j using the LPS table

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Use the LPS table to skip comparisons
            else:
                i += 1

    return indices

# Example text and pattern
text = "ababcabcabababd"
pattern = "ababd"

# Perform KMP search
result = kmp_search(text, pattern)

# Display the results
if result:
    print(f"Pattern found at indices: {result}")
else:
    print("Pattern not found.")
