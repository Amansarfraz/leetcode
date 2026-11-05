class Solution {
  int findTheDistanceValue(List<int> arr1, List<int> arr2, int d) {
    // Sort arr2 to enable fast binary search lookups
    arr2.sort();
    int count = 0;

    for (int num in arr1) {
      if (_isValid(arr2, num, d)) {
        count++;
      }
    }

    return count;
  }

  bool _isValid(List<int> arr, int target, int d) {
    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {
      int mid = left + ((right - left) ~/ 2);
      
      // If the absolute difference is within d, target is invalid
      if ((arr[mid] - target).abs() <= d) {
        return false;
      }
      
      if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return true;
  }
}
