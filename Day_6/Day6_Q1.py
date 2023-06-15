def countRev (s):
    # your code here
    if len(s)%2 == 1:
        return -1
    reversals = 0
    open=0
    for i in range(len(s)):
        if s[i]=='{':
            open=open+1
        else:
            if s[i] != s[i-1]:
                open=open -1
            else:
                reversals = reversals  +1
                open = open +1
    return reversals + open//2


#{ 
 # Driver Code Starts
t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends