
class ProductOfNumbers {
  List<int> _prefixProduct = [];
  int _prefix = 1;
  ProductOfNumbers();

  void add(int num) {
    if (num == 0) {
      _prefixProduct.clear();
      _prefix = 1;
    } else {
      _prefix *= num;
      _prefixProduct.add(_prefix);
    }
  }

  int getProduct(int k) {
    if (k > _prefixProduct.length) return 0;
    if (k == _prefixProduct.length) return _prefix;
    return _prefix ~/ _prefixProduct[_prefixProduct.length - 1 - k];
  }
}
