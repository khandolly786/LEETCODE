class Solution {
  List<String> getLongestSubsequence(List<String> words, List<int> groups) {
    List<String> ans = [];
    int last = -1;
    for (int i = 0; i < words.length; i++) {
      if (groups[i] != last) {
        ans.add(words[i]);
        last = groups[i];
      }
    }
    return ans;
  }
}
