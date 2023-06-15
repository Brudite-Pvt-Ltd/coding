def countAndSay(n: int)->str:
    if n == 1:
        return "1"
    
    prev = countAndSay(n - 1)
    result = ""
    count = 1
    
    for i in range(len(prev)):
        # Check if the current digit is the same as the next digit
        if i + 1 < len(prev) and prev[i] == prev[i + 1]:
            count += 1
        else:
            result += str(count) + prev[i]  # Count and say the digit
            count = 1  # Reset the count for the next digit
    
    return result
n=4
print(countAndSay(n)) 