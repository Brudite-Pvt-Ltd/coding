#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        m={}
        for i in range(0,N):
            if A[i] in m:
                m[A[i]]+=1
            else:
                m[A[i]]=1
        majorityElement = False
        for key in m:
            if m[key]>N/2:
                majorityElement = True
                return key
            else:
                return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends