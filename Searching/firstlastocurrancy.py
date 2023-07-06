arr=[1,2,3,4,4,4,5]
n=len(arr)
x=4
first=0
last=0
for i in range(0,n):
    if arr[i]==x:
        if (first==0):
            first=i
        last=i
print(first,last)