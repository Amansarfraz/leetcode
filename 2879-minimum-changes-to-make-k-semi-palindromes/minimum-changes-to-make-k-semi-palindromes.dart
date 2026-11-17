import 'dart:math';

class Solution {
  int minimumChanges(String s, int k) {
    int n = s.length;
    // factors[len] holds all proper divisors d of len (1 <= d < len)
    List<List<int>> factors = _getFactors(n);
    // cost[i][j] = min changes to make substring s[i..j] a semi-palindrome
    List<List<int>> cost = _getCost(s, n, factors);
    // dp[i][j] = min changes to split s[i..n-1] into j semi-palindromes
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(k + 1, n));

    dp[n][0] = 0;

    for (int i = n - 1; i >= 0; --i) {
      for (int j = 1; j <= k; ++j) {
        // A semi-palindrome must have length at least 2 (since 1 has no proper divisors)
        for (int end = i + 1; end < n; ++end) {
          dp[i][j] = min(dp[i][j], dp[end + 1][j - 1] + cost[i][end]);
        }
      }
    }

    return dp[0][k];
  }

  // Precomputes all proper divisors for every possible substring length up to n
  List<List<int>> _getFactors(int n) {
    List<List<int>> factors = List.generate(n + 1, (_) => []);
    for (int d = 1; d < n; ++d) {
      for (int i = d * 2; i <= n; i += d) {
        factors[i].add(d);
      }
    }
    return factors;
  }

  // Precomputes the minimum cost to turn every substring s[i..j] into a semi-palindrome
  List<List<int>> _getCost(String s, int n, List<List<int>> factors) {
    List<List<int>> cost = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        int len = j - i + 1;
        int minCost = len;
        for (int d in factors[len]) {
          minCost = min(minCost, _calculateCost(s, i, j, d));
        }
        cost[i][j] = minCost;
      }
    }
    return cost;
  }

  // Calculates changes needed for s[i..j] using a specific divisor d
  int _calculateCost(String s, int i, int j, int d) {
    int changes = 0;
    for (int offset = 0; offset < d; ++offset) {
      int l = i + offset;
      int r = j - d + 1 + offset;
      while (l < r) {
        if (s.codeUnitAt(l) != s.codeUnitAt(r)) {
          changes++;
        }
        l += d;
        r -= d;
      }
    }
    return changes;
  }
}
