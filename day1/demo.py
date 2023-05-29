n=[[5,10,19],[2,6,7],[12,13,14]]
print(n)
j=0
k=0
for a in range(3):
    if a == 2:
        break
    else:
        for b in range(3):
            if j == 2 and b == 2:
                break
            print(n[a][b], end=" ")
            if b == 2:
                for a in range(1,3):
                    print(n[a][b], end=" ")
                    j=a
                    if a==2:
                        for b in range(b-1,-1,-1):
                            print(n[a][b], end=" ")