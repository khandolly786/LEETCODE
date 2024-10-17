class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        int n = s.size();

        vector<int> maxRight(n);
        maxRight[n - 1] = n - 1;

        for (int i = n - 2; i >= 0; i--) {
            int rightMaxIdx = maxRight[i + 1];
            maxRight[i] = (s[i] > s[rightMaxIdx]) ? i : rightMaxIdx;
        }

        for (int i = 0; i < n; i++) {
            int maxRightIdx = maxRight[i];
            if (s[i] < s[maxRightIdx]) {
                swap(s[i], s[maxRightIdx]);
                return stoi(s);
            }
        }

        return num;
    }
};
