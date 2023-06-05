//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class Driver
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int []a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();

            int  m= sc.nextInt();
            int []b = new int[m];
            for (int i = 0; i < m; i++) b[i] = sc.nextInt();

            double res = new GFG().medianOfArrays(n, m, a, b);

            if (res == (int)res) System.out.println ((int)res);
            else System.out.println (res);
        }

    }
}
// } Driver Code Ends


//User function Template for Java

class GFG
{
    static double medianOfArrays(int n, int m, int a[], int b[])
    {
        // Your Code Here
        int i = 0;
        int j = 0;
        int count;
        int m1 = -1, m2 = -1;


        if ((m + n) % 2 == 1) {
            for (count = 0; count <= (n + m) / 2; count++) {
                if (i != n && j != m) {
                    m1 = (a[i] > b[j]) ? b[j++]
                            : a[i++];
                }
                else if (i < n) {
                    m1 = a[i++];
                }


                else {
                    m1 = b[j++];
                }
            }
            return m1;
        }


        else {
            for (count = 0; count <= (n + m) / 2; count++) {
                m2 = m1;
                if (i != n && j != m) {
                    m1 = (a[i] > b[j]) ? b[j++]
                            : a[i++];
                }
                else if (i < n) {
                    m1 = a[i++];
                }


                else {
                    m1 = b[j++];
                }
            }
            return (double)((m1 + m2) / 2.0);
        }
    }

}
    
