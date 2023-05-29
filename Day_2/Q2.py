class Solution:
    def getPairsCount(self, arr, n, k):
        count=0# code here
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] + arr[j] == k:
                    count +=1
                else:
                    continue
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1