import 'dart:math';

class Solution {
  int longestMonotonicSubarray(List<int> nums) {
    int maxLength = 1;
    int incLength = 1;
    int decLength = 1;

    for (int i = 1; i < nums.length; i++) {
      if (nums[i] > nums[i - 1]) {
        incLength++;
        decLength = 1;
      } else if (nums[i] < nums[i - 1]) {
        decLength++;
        incLength = 1;
      } else {
        incLength = 1;
        decLength = 1;
      }
      maxLength = max(maxLength, max(incLength, decLength));
    }

    return maxLength;
  }
}
