class Solution {
  int countGood(List<int> nums, int k) {
    Map<int, int> freq = {};
    int left = 0;
    int pairCount = 0;
    int goodSubarrays = 0;

    for (int right = 0; right < nums.length; right++) {
      int num = nums[right];
      pairCount += freq[num] ?? 0;
      freq[num] = (freq[num] ?? 0) + 1;

      while (pairCount >= k) {
        goodSubarrays += nums.length - right;
        int leftNum = nums[left];
        freq[leftNum] = freq[leftNum]! - 1;
        pairCount -= freq[leftNum]!;
        left++;
      }
    }

    return goodSubarrays;
  }
}
