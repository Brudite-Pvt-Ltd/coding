n = int(input("ENTER THE SIZE OF ARRAY \n"))
arr = list(map(int,input().split()))
sub_array = []

for i in range(0,n+1):
    for j in range(i+1,n+1):
        sub_array.append(arr [i : j])
    # print(sub_array)
for i in sub_array:
    if sum(i) == 13:
        print(i)
   