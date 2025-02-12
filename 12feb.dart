import 'dart:collection';
import 'dart:math';

class Solution {
  int maximumSum(List<int> nums) {
    int res = -1;
    final Map<int, int> freq = {};

    for (int i in nums) {
      int key = digitSum(i);
      if (freq.containsKey(key)) {
        int old = freq[key]!;
        res = max(res, old + i);
        freq[key] = max(old, i);
      } else {
        freq[key] = i;
      }
    }
    return res;
  }

  int digitSum(int n) {
    int sum = 0;
    while (n > 0) {
      sum += n % 10;
      n = n ~/ 10;
    }
    return sum;
  }
}
