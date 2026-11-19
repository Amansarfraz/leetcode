import 'dart:math';

class Solution {
  int minimizeSum(List<int> nums) {
    nums.sort();
    int n = nums.length;

    int option1 = nums[n - 3] - nums[0];
    int option2 = nums[n - 1] - nums[2];
    int option3 = nums[n - 2] - nums[1];

    return min(option1, min(option2, option3));
  }
}
