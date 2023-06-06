//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0)
        {
            String s, patt;
            s = sc.next();
            patt = sc.next();
            
            Solution ob = new Solution();
            
            ArrayList<Integer> res = ob.search(patt, s);
            
            for(int i = 0;i<res.size();i++)
                System.out.print(res.get(i) + " ");
            System.out.println();    
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{
    
    ArrayList<Integer> search(String pat, String S)
    {
        // your code here
        int d = 256;
        int h = 1;
        int p = 0, t = 0;
        int q = 11;
        
        for (int i = 0; i < pat.length() - 1; i++) {
            h = (h * d) % q;
        }
        
        for (int i = 0; i < pat.length(); i++) {
            p = ((d * p) + pat.charAt(i)) % q;
            t = ((d * t) + S.charAt(i)) % q;
        }
        int N = S.length();
        int M = pat.length();
        ArrayList<Integer> al = new ArrayList<>();
        for (int i = 0; i <= N - M; i++) {
            if (p == t) {
                int j = 0;
                for (j = 0; j < pat.length(); j++) {
                    if (S.charAt(i + j) != pat.charAt(j)) {
                        break;   
                    }
                }
                if (j == M) {
                    al.add(i + 1);
                }
            }
            if (i < N - M) {
                t = ((d * (t - (S.charAt(i) * h))) + S.charAt(i + M)) % q;
            }
            
            if (t < 0) {
                t += q;
            }
        }
        if (al.size() == 0) {
            al.add(-1);
            return al;
        }
        return al;
    }
}
        
    
