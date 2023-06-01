a = "GEEKSFORGEEKS"
B = {}

for i in a:
    if i not in B:
        B[i] = 1
    else:
        B[i] += 1
for i in B:
    if B[i] > 1:
        print(i,"-",B[i])
    else:
        pass
            