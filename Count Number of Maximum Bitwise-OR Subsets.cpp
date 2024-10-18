class Solution {
public:
int countSubsets(int idx, int currOR, vector<int>& nums, int maxOR){
    if(idx== nums.size()){
        if(currOR== maxOR)
             return 1;
        return 0;
    }
    //Taking num[idx]
    int takecount = countSubsets(idx+1, currOR| nums[idx], nums, maxOR);
    int notcount = countSubsets(idx+1, currOR, nums, maxOR);

    return takecount+notcount;
    }
    int countMaxOrSubsets(vector<int>& nums) {
        int maxOR = 0;
        for(int &num : nums){
        maxOR |= num;
        }
        int currOR = 0;
        return countSubsets(0, currOR, nums, maxOR);
    }
};
