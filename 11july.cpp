class Solution {
  public:
    int countConsec(int n) {
        int prev=0;
        int curr=1;
        int ans=1;
        for(int i=2; i<n; i++){
            int next=prev+curr;
            ans= ans*2+next;
            prev=curr;
            curr=next;
        }
        return ans;
    }
};
