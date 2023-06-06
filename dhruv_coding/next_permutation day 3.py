#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        i = j = N - 1
        idx1 = 0
        idx2 = 0
		
        while i >= 1:
            if arr[i-1] < arr[i]:
                idx1 = i-1
                break
            i -= 1
			
        while j >= 1:
            if arr[j] > arr[idx1]:
                idx2 = j
                break
            j -= 1
			
        if idx1 == 0 and idx2 == 0:  # arr is in descending order
            k = 0
            l = N - 1
            while k < l:
                arr[k], arr[l] = arr[l], arr[k]
                k += 1
                l -= 1
            return arr
			
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        k = idx1 + 1
        l = len(arr) - 1
        while k < l:
            arr[k], arr[l] = arr[l], arr[k]
            k += 1
            l -= 1
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends