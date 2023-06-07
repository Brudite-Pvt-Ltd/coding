Col = int(input("c"))
Row = int(input("enter the trusted person"))
m = [[int(input()) for x in range(Col)] for y in range(Row)]
print(m)
n = len(m)
dict = {}
list = []
for i in range(n):
    list.append(m[i][1])
for j in list:
    if j not in dict:
        dict[j] = 1
    else:
        dict[j] += 1
print(dict)
maxi = max(dict, key=dict.get)
print()
