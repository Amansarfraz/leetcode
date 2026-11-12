class Solution {
  String processStr(String s) {
    List<String> result = [];
    for (int i = 0; i < s.length; i++) {
      String c = s[i];
      if (c == '*') {
        if (result.isNotEmpty) {
          result.removeLast();
        }
      } else if (c == '#') {
        result.addAll(List.from(result));
      } else if (c == '%') {
        result = result.reversed.toList();
      } else {
        result.add(c);
      }
    }
    return result.join();
  }
}

