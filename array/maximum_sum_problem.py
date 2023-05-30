arr=[1,2,3,-2,5]
N=len(arr)
sum=0
maxi=arr[0]
for i in range(0,N):
    sum=sum+arr[i]
    maxi=max(maxi,sum)
    if sum<0:
        sum=0
    

print(maxi)