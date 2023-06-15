def removeDuplicates(s):
    result = s[0]  # Initialize the result with the first character
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            result += s[i]
    return result
