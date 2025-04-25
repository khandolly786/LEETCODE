class Solution {
    static int majorityElement(int arr[]) {
        int x = -1;
        int count = 0;
        for (int val : arr) {
            if (count == 0) {
                x = val;
                count = 1;
            } else if (x == val) {
                count++;
            } else {
                count--;
            }
        }
        
        count = 0;
        for (int val : arr) {
            if (x == val) {
                count++;
            }
        }
        
        if (count > arr.length / 2) {
            return x;
        }
        return -1;
    }
}
