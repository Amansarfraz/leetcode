import 'dart:math';

class Solution {
  int minimumSumSubarray(List<int> nums, int l, int r) {
    // Maximum possible sum is 100 * 1000 = 100,000, so 1000000 acts as infinity
    int minSum = 1000000; 
    int n = nums.length;

    for (int i = 0; i < n; i++) {
      int currentSum = 0;
      for (int j = i; j < n; j++) {
        currentSum += nums[j];
        int length = j - i + 1;

        if (length >= l && length <= r) {
          if (currentSum > 0) {
            minSum = min(minSum, currentSum);
          }
        }
      }
    }

    return minSum == 1000000 ? -1 : minSum;
  }
}
