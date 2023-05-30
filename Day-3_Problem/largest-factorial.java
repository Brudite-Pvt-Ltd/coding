

import java.io.*;
import java.util.*;

class GfG
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0)
        {
            int N = sc.nextInt();
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.factorial(N);
            for (Integer val: ans) 
                System.out.print(val); 
            System.out.println();
        }   
    }
}


class Solution {
    static ArrayList<Integer> factorial(int N){
        //code here
        ArrayList<Integer> al =new ArrayList<>();
        int size=1,c=0;
        al.add(0,1);
        int val=2;
        while(val<=N){
            for(int i=size-1;i>=0;i--){
                int temp=al.get(i)*val +c;
                al.set(i,temp%10);
                c=temp/10;
            }
            while(c!=0){
                al.add(0,c%10);
                c=c/10;
                size++;
            }
            val++;
    }
    return al;
}
}