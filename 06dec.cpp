class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        int sum=0; 
        int cnt=0;

        unordered_set<int> st(begin(banned), end(banned));
        for(int num=1; num<=n; num++){
            if(st.count(num)){
                continue;
            }
            if(sum+num <=maxSum){
                sum+=num;
                cnt++;
            }
            else{
                break;
            }
        }
        return cnt;
        
    }
};
