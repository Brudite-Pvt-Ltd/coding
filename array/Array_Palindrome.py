# def PalinArray(arr ,n):
#     # Code here
#     for i in range(0,n):
        
#         temporiginal=arr[i]
#         rev=0
#         while temporiginal<0:
#             ld=temporiginal%10
#             rev=rev*10+ld
#             temporiginal=temporiginal/10
#         if rev!=arr[i]:
#             return 0
    
#     return 1    



# #{ 
#  # Driver Code Starts
# # Driver Program
# if __name__=='__main__':
#     t=int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int, input().strip().split()))
#         if PalinArray(arr, n):
#             print(1)
#         else:
#             print(0)


# # } Driver Code Ends
def PalinArray(arr ,n):
    # Code here
    count=0
    for i in range(0,n):
        a=str(arr[i])
        if (a==a[::-1]):
            count+=1
    if count==n:
        return 1
    else:
        return 0
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)