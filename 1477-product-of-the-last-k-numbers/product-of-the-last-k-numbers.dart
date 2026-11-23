class ProductOfNumbers {
  final List<int> _prefix = <int>[];

  ProductOfNumbers() {
    _prefix.add(1);
  }

  void add(int num) {
    if (num == 0) {
      _prefix
        ..clear()
        ..add(1);
    } else {
      _prefix.add(_prefix.last * num);
    }
  }

  int getProduct(int k) {
    final int n = _prefix.length;
    if (k >= n) {
      return 0;
    }
    return _prefix.last ~/ _prefix[n - 1 - k];
  }
}
