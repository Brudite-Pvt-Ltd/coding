class Solution:
    def sort012(self,arr,n):
        for i in range(1,len(arr)):
            j = i
            while arr[j-1] > arr[j] and j>0:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j -= 1
            
                
                
                
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()