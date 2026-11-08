class Solution {
  int countServers(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;

    // Track the total number of servers in each row and column
    List<int> rowCount = List.filled(m, 0);
    List<int> colCount = List.filled(n, 0);

    // First pass: Count how many servers exist in each row and column
    for (int r = 0; r < m; r++) {
      for (int c = 0; c < n; c++) {
        if (grid[r][c] == 1) {
          rowCount[r]++;
          colCount[c]++;
        }
      }
    }

    int communicatingServers = 0;

    // Second pass: Count servers that share a row or column with at least one other server
    for (int r = 0; r < m; r++) {
      for (int c = 0; c < n; c++) {
        if (grid[r][c] == 1) {
          if (rowCount[r] > 1 || colCount[c] > 1) {
            communicatingServers++;
          }
        }
      }
    }

    return communicatingServers;
  }
}
