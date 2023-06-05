def ss(s, ans):
    if len(s) == 0:
        print(ans)
        return

    c = s[0]
    s = s[1:]
    ss(s, ans + c)
    ss(s, ans)


s = input()
ans = ""
ss(s, ans)
