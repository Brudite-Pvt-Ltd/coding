package day1;

import java.util.*;
// import java.io.*;
// import java.lang.*;

public class count_inversion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long t = sc.nextLong();

        while (t-- > 0) {
            long n = sc.nextLong();
            long arr[] = new long[(int) n];

            for (long i = 0; i < n; i++)
                arr[(int) i] = sc.nextLong();

            System.out.println(new Solution().inversionCount(arr, n));

        }
    }

}

// } Driver Code Ends

// User function Template for Java

class Solution {

    long inversionCount(long arr[], long N) {

        long count = 0;
        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                if (arr[i] > arr[j]) {
                    count++;
                }
            }
        }
        return count;

    }
}
