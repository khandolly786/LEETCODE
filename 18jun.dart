class Solution {
  List<List<int>> divideArray(List<int> nums, int k) {
    nums.sort();
    int size = nums.length;
    List<List<int>> sol = [];

    for (int i = 0; i < size; i += 3) {
      if (i + 2 >= size || nums[i + 2] - nums[i] > k) return [];
      sol.add([nums[i], nums[i + 1], nums[i + 2]]);
    }

    return sol;
  }
}
