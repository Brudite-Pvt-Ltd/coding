class Solution:
    def minFlips(self, S):
        # Code here
        
  
        count1 = 0
        count2 = 0
        
        for i in range(len(S)):
            if i % 2 == 0:
                if S[i] != '0':
                    count1 += 1
            else:
                if S[i] != '1':
                    count1 += 1
        
        for j in range(len(S)):
            if j % 2 == 0:
                if S[j] != '1':
                    count2 += 1
            else:
                if S[j] != '0':
                    count2 += 1
        
        min1 = min(count1, count2)
        return min1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends