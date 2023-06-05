s = "leetcode"
WordDict = ["leet", "code"]
a = len(s)

for i in WordDict:
    len_i = len(i)
    for j in range(0, a, len_i):
        if i == j:
            print(True)
        else:
            print("you are doing wrong")
