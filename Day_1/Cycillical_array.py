def rotate(arr):
    n = len(a)
    x = arr[n-1]                  #5
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = x
    return arr
def Rotate_2(b):
    m = len(b)
    z = b[m-1]
    for j in range(m-1,0,-1):
        b[j] = b[j-1]
    b[0] = z
    return b
def Rotate_3(c):
    o = len(c)
    l = c[o-1]
    for k in range(o-1,0,-1):
        c[k] = c[k-1]
    c[0] = l
    return c
a = list(map(int,input("Enter the input please").split()))
b = rotate(a)
print(b)
d = Rotate_2(b)
print(d)
e = Rotate_3(d)
print(e)