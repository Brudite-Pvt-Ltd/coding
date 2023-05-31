a=[1,2,3,-4,-1,4]
n=len(a)
i=a[0]
j=a[n-1]
while(i<j):
    if a[i]>0:
        i+=1
    if a[j]<0:
        j-=1
    else:
        temp=0
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
print(a)
k=0

# a=[1,2,3,-4,-1,4]
# n=len(a)
# b=[]
# c=[]
# for i in range(0,n):
#     if a[i]>0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(b)
# print(c)
# e=[]
# for k in range(0,n):
#     e.append(b[k])
#     for j in range(i):
#         e.append(c[j])
    
# print(e)

