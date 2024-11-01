class Solution {
public:
    string makeFancyString(string s) {
        string output ="";
        if(s.size()<=2){
            return s;
        }
        for(int i=0; i<s.size()-2; i++){
            if(s[i]==s[i+1] && s[i]==s[i+2]){
                continue;
            }
            output+= s[i];
        }
        output +=s[s.size()-2];
        output +=s[s.size()-1];
        return output;
    }
};
