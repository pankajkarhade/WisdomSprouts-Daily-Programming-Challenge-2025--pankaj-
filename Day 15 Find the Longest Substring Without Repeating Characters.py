def length_of_longest_substring(s: str) -> int:
  char_index_map = {}
  max_length = 0
  left = 0
  for right, char in enumerate(s):
    if char in char_index_map and char_index_map[char] >= left:
      left = char_index_map[char] + 1
    char_index_map[char] = right
    current_length = right - left + 1
    max_length = max(max_length, current_length)   
  return max_length

# Test :-
test_cases = [
    {"input": "abcabcbb", "expected": 3},
    {"input": "bbbbb", "expected": 1},
    {"input": "pwwkew", "expected": 3},
    {"input": "abcdefgh", "expected": 8},
    {"input": "a", "expected": 1},
    {"input": "", "expected": 0}]
for i, test in enumerate(test_cases):
    input_str = test['input']
    expected = test['expected']
    actual = length_of_longest_substring(input_str)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: "{input_str}"')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
