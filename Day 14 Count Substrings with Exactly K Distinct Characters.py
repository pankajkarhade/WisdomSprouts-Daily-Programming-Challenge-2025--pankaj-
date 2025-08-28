import collections
def count_substrings_with_k_distinct(s: str, k: int) -> int:
  return count_at_most_k(s, k) - count_at_most_k(s, k - 1)

def count_at_most_k(s: str, k: int) -> int:
  if k < 0:
    return 0 
  n = len(s)
  left = 0
  total_count = 0
  char_counts = collections.defaultdict(int)
  for right in range(n):
    char_counts[s[right]] += 1
    while len(char_counts) > k:
      left_char = s[left]
      char_counts[left_char] -= 1
      if char_counts[left_char] == 0:
        del char_counts[left_char]
      left += 1
    total_count += (right - left + 1)
  return total_count
  
#  Test  :-
test_cases = [
    {"s": "pqpqs", "k": 2, "expected": 7},
    {"s": "aabacbebebe", "k": 3, "expected": 10},
    {"s": "a", "k": 1, "expected": 1},
    {"s": "abc", "k": 3, "expected": 1},
    {"s": "abc", "k": 2, "expected": 2},]
for i, test in enumerate(test_cases):
    s_input = test['s']
    k_input = test['k']
    expected = test['expected']
    actual = count_substrings_with_k_distinct(s_input, k_input)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: s="{s_input}", k={k_input}')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
