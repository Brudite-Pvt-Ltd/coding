
def valueEqualToIndex(self, arr, n):
    result = []
    for i in range(len(arr)):
        # As the array follows 1-based indexing, we compare (i+1) with arr[i]
        if arr[i] == (i+1):
            result.append(arr[i])
    return result
