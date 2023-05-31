#User function Template for python3


def find_median(v):
    v.sort()
    s = int(len(v))
    h = int(s//2)
    if s % 2 == 0:
        return int(v[h-1] + v[h])//2
    else :
        return int(v[h])
  
a = list(map(int,input("enter the array values").split()))
b = find_median(a)
print(b)