class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.size();
        unordered_set<char> letters(s.begin(), s.end());
        int result = 0;

        for (char letter : letters) {
            int leftidx = -1, rightidx = -1;

            // Find the first and last occurrence of the current letter
            for (int i = 0; i < n; i++) {
                if (s[i] == letter) {
                    if (leftidx == -1) {
                        leftidx = i;
                    }
                    rightidx = i;
                }
            }

            if (leftidx < rightidx) { // Ensure there's a valid range for middle characters
                unordered_set<char> st;

                // Collect unique characters between the first and last occurrence
                for (int middle = leftidx + 1; middle < rightidx; middle++) {
                    st.insert(s[middle]);
                }

                result += st.size(); // Add the count of unique middle characters
            }
        }

        return result;
    }
};
