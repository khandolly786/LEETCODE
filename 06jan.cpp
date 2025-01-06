class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n=boxes.size();
        vector<int> answer(n, 0);
        int cumValue=0;
        int cumValuesum=0;

        for(int i=0; i<n; i++){
            answer[i] = cumValuesum;

            cumValue+=boxes[i]=='0'? 0 :1;

            cumValuesum+=cumValue;
        }
        cumValue=0;
        cumValuesum=0;
        for(int i=n-1; i>=0; i--){
            answer[i]+= cumValuesum;

            cumValue+=boxes[i]=='0'?0:1;

            cumValuesum+=cumValue;
        }

        return answer;
    }
};
