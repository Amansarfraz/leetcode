import 'dart:math';

class Solution {
  int maximumSaleItems(List<List<int>> items, int budget) {
    const int maxFactor = 1500;
    List<int> freq = List.filled(maxFactor + 1, 0);

    int minPrice = 1000000000;
    for (var item in items) {
      freq[item[0]]++;
      if (item[1] < minPrice) {
        minPrice = item[1];
      }
    }

    // Har factor f ke liye kitne items hain jinhe f divide karta hai
    List<int> divCount = List.filled(maxFactor + 1, 0);
    for (int f = 1; f <= maxFactor; f++) {
      if (freq[f] == 0) continue;
      int total = 0;
      for (int m = f; m <= maxFactor; m += f) {
        total += freq[m];
      }
      divCount[f] = total;
    }

    // 0-1 Knapsack: har item ki pehli copy lene par (1 + free_i) copies milti hain
    List<int> dp = List.filled(budget + 1, 0);

    for (var item in items) {
      int f = item[0];
      int price = item[1];
      if (price > budget) continue;

      int value = divCount[f]; // 1 (khud) + (divCount[f] - 1) (free copies) = divCount[f]

      for (int b = budget; b >= price; b--) {
        int cand = dp[b - price] + value;
        if (cand > dp[b]) {
          dp[b] = cand;
        }
      }
    }

    // Kisi bhi state mein bache hue budget se sabse saste item ki extra copies le sakte hain
    int ans = 0;
    for (int b = 0; b <= budget; b++) {
      int extraCopies = (budget - b) ~/ minPrice;
      int total = dp[b] + extraCopies;
      if (total > ans) {
        ans = total;
      }
    }

    return ans;
  }
}