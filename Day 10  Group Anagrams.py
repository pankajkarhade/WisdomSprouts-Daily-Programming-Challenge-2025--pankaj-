import collections
def group_anagrams(strs: list[str]) -> list[list[str]]:
  anagram_map = collections.defaultdict(list)
  for word in strs:
    sorted_word_key = "".join(sorted(word))
    anagram_map[sorted_word_key].append(word)
  return list(anagram_map.values())

#Test cases :-
test_cases = [
    {"input": ["eat", "tea", "tan", "ate", "nat", "bat"]},
    {"input": [""]},
    {"input": ["a"]},
    {"input": ["abc", "bca", "cab", "xyz", "zyx", "yxz"]},
    {"input": ["abc", "def", "ghi"]},]
for i, test in enumerate(test_cases):
    input_strs = test['input']
    actual_output = group_anagrams(input_strs)  
    actual_output_sorted = sorted([sorted(group) for group in actual_output])    
    print(f"\nTest Case {i + 1} :-")
    print(f"Input: {input_strs}")
    print(f"Output: {actual_output}")
