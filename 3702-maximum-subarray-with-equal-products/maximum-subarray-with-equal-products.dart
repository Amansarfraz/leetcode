import 'dart:math';

class Solution {
  int maxLength(List<int> nums) {
    final int n = nums.length;
    int maxLen = 1;
    // Max possible value of lcm(1..10) * max_gcd(10) = 2520 * 10 = 25200
    const int maxLimit = 25200;

    for (int i = 0; i < n; i++) {
      int prod = nums[i];
      int currentGcd = nums[i];
      int currentLcm = nums[i];

      for (int j = i + 1; j < n; j++) {
        prod *= nums[j];
        if (prod > maxLimit) {
          break;
        }
        currentGcd = _gcd(currentGcd, nums[j]);
        currentLcm = (currentLcm * nums[j]) ~/ _gcd(currentLcm, nums[j]);

        if (prod == currentLcm * currentGcd) {
          maxLen = max(maxLen, j - i + 1);
        }
      }
    }

    return maxLen;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
}
