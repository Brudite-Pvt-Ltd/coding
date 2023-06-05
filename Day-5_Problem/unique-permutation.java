//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
	public static void main(String[] args) throws IOException
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0)
        {
            String S = br.readLine().trim();
            Solution obj = new Solution();
            List<String> ans = obj.find_permutation(S);
            for( int i = 0; i < ans.size(); i++)
            {
                out.print(ans.get(i)+" ");
            }
            out.println();
                        
        }
        out.close();
	}
}


// } Driver Code Ends


class Solution {
    List<String> list = new ArrayList<>();
    public List<String> find_permutation(String S) {
        permute(S, 0, S.length() - 1);
         Collections.sort(list);
        return list;
    }
    
     private void permute(String str, int l, int r) {
        if (l == r) {
            if (!list.contains(str)) {
                list.add(str);
            }

            return;
        }
        for (int i = l; i <= r; i++) {
            str = swap(str, l, i);
            permute(str, l + 1, r);
            str = swap(str, l, i);
        }
    }
    
     private String swap(String str, int i, int j) {
        char[] chare = str.toCharArray();
        char temp = chare[i];
        chare[i] = chare[j];
        chare[j] = temp;
        return String.valueOf(chare);
    }
    
    }
