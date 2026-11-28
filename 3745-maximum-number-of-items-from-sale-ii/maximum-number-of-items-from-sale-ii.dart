import 'dart:math';

class Solution {
  int maximumSaleItems(List<List<int>> items, int budget) {
    int n = items.length;
    if (n == 0 || budget <= 0) return 0;

    // 1. Har factor ki frequency aur sabse kam price nikalen
    List<int> freq = List.filled(n + 1, 0);
    int minPrice = items[0][1];

    for (var item in items) {
      int f = item[0];
      int p = item[1];
      if (f <= n) freq[f]++;
      if (p < minPrice) minPrice = p;
    }

    // 2. Har factor f ke liye valid targets ki count (khud ko exclude karke)
    List<int> degForFactor = List.filled(n + 1, 0);
    for (int f = 1; f <= n; f++) {
      if (freq[f] == 0) continue;
      int total = 0;
      for (int m = f; m <= n; m += f) {
        total += freq[m];
      }
      degForFactor[f] = total - 1;
    }

    // Har double-deal unit: [price, count] jahan har unit cost `price` par `2` items deta hai
    List<List<int>> cheapDoubleDeals = [];
    List<List<int>> costlyDoubleDeals = [];

    for (var item in items) {
      int f = item[0];
      int p = item[1];
      int d = degForFactor[f];
      if (d > 0 && p <= budget) {
        if (p < 2 * minPrice) {
          cheapDoubleDeals.add([p, d]);
        } else {
          costlyDoubleDeals.add([p, d]);
        }
      }
    }

    cheapDoubleDeals.sort((a, b) => a[0].compareTo(b[0]));
    costlyDoubleDeals.sort((a, b) => a[0].compareTo(b[0]));

    int ans = 0;
    int remBudget = budget;

    // Pehle un double-deals ko lein jo minPrice se better ratio (2/p > 1/minPrice) dete hain
    for (var deal in cheapDoubleDeals) {
      int p = deal[0];
      int d = deal[1];
      int take = min(d, remBudget ~/ p);
      ans += take * 2;
      remBudget -= take * p;
    }

    // Phir bache budget se minPrice wale single items lein
    int singleTake = remBudget ~/ minPrice;
    ans += singleTake;
    remBudget -= singleTake * minPrice;

    // Aakhir mein agar budget bacha ho toh costlyDoubleDeals try karein
    for (var deal in costlyDoubleDeals) {
      int p = deal[0];
      int d = deal[1];
      int take = min(d, remBudget ~/ p);
      ans += take * 2;
      remBudget -= take * p;
    }

    return ans;
  }
}