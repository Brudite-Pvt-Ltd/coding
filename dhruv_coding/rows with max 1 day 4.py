#User function Template for python3
class Solution:
    def rowWithMax1s(self,arr, n, m):
        max_row_index = -1
        max_ones_count = 0
        j = m - 1

        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                j -= 1

            if j < m - 1:
                ones_count = m - 1 - j
                if ones_count > max_ones_count:
                    max_ones_count = ones_count
                    max_row_index = i

        return max_row_index
    
    
    
    
    
    #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends