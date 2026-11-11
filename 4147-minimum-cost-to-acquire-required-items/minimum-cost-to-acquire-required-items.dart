import 'dart:math';

class Solution {
  int minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
    // Strategy 1: Buy everything completely individually
    int option1 = (need1 * cost1) + (need2 * cost2);
    
    // Strategy 2: Buy bundles exactly up to the required match, then leftovers individually
    int exactBundles = min(need1, need2);
    int option2 = (exactBundles * costBoth) 
                + ((need1 - exactBundles) * cost1) 
                + ((need2 - exactBundles) * cost2);
                
    // Strategy 3: Over-buy bundles to satisfy the larger requirement (wasting the extra items)
    int extraBundles = max(need1, need2);
    int option3 = extraBundles * costBoth;
    
    // Return the absolute cheapest strategy
    return min(option1, min(option2, option3));
  }
}
