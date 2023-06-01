import math
def find(n,k,arr):
    a = n/k
    final = []
    for i in arr:
        if arr.count(i) >= a and i  not in final:
            final.append(i)
    print(final)
k = 3
n = 7
arr=[4,5,6,7,8,4,4,5,6,5]
find(n,k,arr)

    