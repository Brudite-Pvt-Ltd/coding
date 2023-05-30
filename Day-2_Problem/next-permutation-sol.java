class Solution {
    public void nextPermutation(int[] nums) {
        int n=nums.length;
        int idx=-1;
        for(int i=n-2;i>=0;i--){
            if(nums[i]<nums[i+1]){
               idx=i;
                break;
            }
        }

            for(int i=n-1;i>=0 && idx!=-1;i--){
                if(nums[i]>nums[idx]){
                    int temp=nums[idx];
                    nums[idx]=nums[i];
                    nums[i]=temp;
                    break;
                }
            }
            int l=idx+1,r=n-1;
            while(l<r){
                int temp=nums[l];
                nums[l]=nums[r];
                nums[r]=temp;
                l++;r--;
            }
            
        }  
    }
    