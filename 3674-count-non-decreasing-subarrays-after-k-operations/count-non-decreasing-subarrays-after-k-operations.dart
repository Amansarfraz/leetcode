import 'dart:collection';

class Solution {
  int countNonDecreasingSubarrays(List<int> nums, int k) {
    int ans = 0;
    int cost = 0;
    var dq = Queue<int>();
    int j = nums.length - 1;

    for (int i = nums.length - 1; i >= 0; i--) {
      int num = nums[i];
      while (dq.isNotEmpty && nums[dq.last] < num) {
        int l = dq.removeLast();
        int r = dq.isEmpty ? j + 1 : dq.last;
        cost += (r - l) * (num - nums[l]);
      }
      dq.addLast(i);

      while (cost > k) {
        cost -= nums[dq.first] - nums[j];
        if (dq.first == j) {
          dq.removeFirst();
        }
        j--;
      }
      ans += j - i + 1;
    }

    return ans;
  }
}
