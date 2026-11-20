import 'dart:math';
import 'dart:typed_data';

class Solution {
  int maxSelectedElements(List<int> nums) {
    nums.sort();
    
    // Max possible value is 10^6 + 1, so size 1000003 safely covers all indices
    final dp = Int32List(1000003);
    int maxLen = 0;

    for (final x in nums) {
      // Must update x + 1 before x so the same element isn't used twice
      dp[x + 1] = max(dp[x + 1], dp[x] + 1);
      dp[x] = max(dp[x], dp[x - 1] + 1);
      
      maxLen = max(maxLen, max(dp[x], dp[x + 1]));
    }

    return maxLen;
  }
}
