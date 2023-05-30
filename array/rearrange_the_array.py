# a=[1,2,3,-4,-1,4]
# n=len(a)
# i=0
# j=n
# while(i<j):
#     if i>0:
#         i+=1
#     if j<0:
#         j+=1
#     else:
#         temp=0
#         temp=a[i]
#         a[i]=a[j]
#         a[j]=temp
# print(a)
#     k=0
#     while(k<n and i<n):
#         i+=1
#         k+=2
#         t=0
#         t=a[i]
#         a[i]=a[k]
#         a[k]=temp
# print(a)
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

def rightRotate(arr, n, outOfPlace, cur):
	temp = arr[cur]
	for i in range(cur, outOfPlace, -1):
		arr[i] = arr[i - 1]
	arr[outOfPlace] = temp
	return arr


def rearrange(arr, n):
	outOfPlace = -1
	for index in range(n):
		if(outOfPlace >= 0):
			if((arr[index] >= 0 and arr[outOfPlace] < 0) or
			(arr[index] < 0 and arr[outOfPlace] >= 0)):
				arr = rightRotate(arr, n, outOfPlace, index)
				if(index-outOfPlace > 2):
					outOfPlace += 2
				else:
					outOfPlace = - 1

		if(outOfPlace == -1):
			if((arr[index] >= 0 and index % 2 == 0) or
			(arr[index] < 0 and index % 2 == 1)):
				outOfPlace = index
	return arr
arr = [-5, -2, 5, 2, 4,
	7, 1, 8, 0, -8]

print("Given Array is:")
print(arr)

print("\nRearranged array is:")
print(rearrange(arr, len(arr)))

