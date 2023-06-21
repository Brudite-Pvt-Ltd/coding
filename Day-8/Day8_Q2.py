class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        arr.sort()
        count = 0
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                tripletSum = arr[i] + arr[left] + arr[right]

                if tripletSum < sumo:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count


#{ 
 # Driver Code Starts

t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    k=l[1]
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.countTriplets(a,n,k)
    print(ans)
# } Driver Code Ends