class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        int m= s.size();
        int n= spaces.size();
        string result="";
        int j=0; //spaces array ke traverse karne ke liye ye karna pad rha h
        for(int i=0;i<m; i++){
            if(j<n && i==spaces[j]){
                result+= " ";
                j++;
            }
            result+=s[i];
        }
        return result;
    }
};
