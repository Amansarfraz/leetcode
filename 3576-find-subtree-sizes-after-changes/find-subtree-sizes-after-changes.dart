import 'dart:typed_data';

class Solution {
  List<int> findSubtreeSizes(List<int> parent, String s) {
    final int n = parent.length;

    // Build initial adjacency list
    final List<List<int>> adj = List.generate(n, (_) => <int>[]);
    for (int i = 1; i < n; i++) {
      adj[parent[i]].add(i);
    }

    final Int32List newParent = Int32List.fromList(parent);
    final Int32List lastSeen = Int32List(26)..fillRange(0, 26, -1);

    // 1. Iterative DFS with backtracking to find closest matching ancestors
    // Stack entries: positive/zero = enter node u, negative (~u) = exit node u
    final List<int> stack = <int>[0];
    final Int32List prevSeen = Int32List(n);

    while (stack.isNotEmpty) {
      final int curr = stack.removeLast();
      if (curr >= 0) {
        final int u = curr;
        final int c = s.codeUnitAt(u) - 97;

        if (lastSeen[c] != -1) {
          newParent[u] = lastSeen[c];
        }

        prevSeen[u] = lastSeen[c];
        lastSeen[c] = u;

        // Push exit marker before children so it runs after all children finish
        stack.add(~u);
        for (final int v in adj[u]) {
          stack.add(v);
        }
      } else {
        final int u = ~curr;
        final int c = s.codeUnitAt(u) - 97;
        lastSeen[c] = prevSeen[u];
      }
    }

    // 2. Build final tree and compute subtree sizes in post-order
    final List<List<int>> newAdj = List.generate(n, (_) => <int>[]);
    for (int i = 1; i < n; i++) {
      newAdj[newParent[i]].add(i);
    }

    final List<int> ans = List<int>.filled(n, 1);
    final List<int> order = <int>[];
    stack.add(0);

    while (stack.isNotEmpty) {
      final int u = stack.removeLast();
      order.add(u);
      for (final int v in newAdj[u]) {
        stack.add(v);
      }
    }

    // Traverse in reverse topological order to accumulate subtree sizes
    for (int i = order.length - 1; i > 0; i--) {
      final int u = order[i];
      ans[newParent[u]] += ans[u];
    }

    return ans;
  }
}
