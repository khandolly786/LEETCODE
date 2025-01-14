class Solution {
    // Function to find equilibrium point in the array.
    public static int findEquilibrium(int arr[]) {
        // code here
        int sum=0;
        for(int x: arr)
        {
            sum+=x;
        }
        
        int left=0;
        int right=0;
        
        for(int x=0;x<arr.length;x++)
        {
            right= sum-left-arr[x];
            if(left==right)
            {
                return x;
            }
            left+= arr[x];
        }
        return -1;
    }
}
