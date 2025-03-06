class Solution {
  List<int> findMissingAndRepeatedValues(List<List<int>> grid) {
  List<int> repeatedWords = [];
  List<int> allNumbers = [];
  for(var lists in grid){
    allNumbers.addAll(lists);
  }

  List<int> list = [];
  int length = allNumbers.length;

  for(int i = 0; i < allNumbers.length; i++){
    if(list.contains(allNumbers[i])){
      repeatedWords.add(allNumbers[i]);
    }else{
      list.add(allNumbers[i]);
    }
  }

  for(int i = 1; i <= length; i++){
    if(!list.contains(i)){
      repeatedWords.add(i);
    }
  }
  
  return repeatedWords;
}
}
