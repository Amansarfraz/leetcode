class Solution {
  int numOfSubarrays(List<int> arr) {
    const int mod = 1000000007;
    
    // Start with evenCount = 1 to represent an empty prefix sum of 0 (which is even).
    int evenCount = 1;
    int oddCount = 0;
    
    int currentSum = 0;
    int totalOddSubarrays = 0;

    for (int num in arr) {
      currentSum += num;

      if (currentSum % 2 == 0) {
        // An even prefix sum minus any previous odd prefix sum yields an odd subarray sum.
        totalOddSubarrays = (totalOddSubarrays + oddCount) % mod;
        evenCount++;
      } else {
        // An odd prefix sum minus any previous even prefix sum yields an odd subarray sum.
        totalOddSubarrays = (totalOddSubarrays + evenCount) % mod;
        oddCount++;
      }
    }

    return totalOddSubarrays;
  }
}
