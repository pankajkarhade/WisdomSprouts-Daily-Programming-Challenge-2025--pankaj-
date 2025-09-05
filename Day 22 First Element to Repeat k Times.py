import collections
def find_first_k_repeat(arr: list[int], k: int) -> int:
  frequency_map = collections.Counter(arr)
  for num in arr:
    if frequency_map[num] == k:
      return num  
  return -1

# Test Harness :-
test_cases = [
    {"arr": [3, 1, 4, 4, 5, 2, 6, 1, 4], "k": 2, "expected": 1},
    {"arr": [2, 3, 4, 2, 2, 5, 5], "k": 2, "expected": 5},
    {"arr": [1, 1, 1, 1], "k": 1, "expected": -1},
    {"arr": [10], "k": 1, "expected": 10},
    {"arr": [6, 6, 6, 6, 7, 7, 8, 8, 8], "k": 3, "expected": 8},]
for i, test in enumerate(test_cases):
    arr_input = test['arr']
    k_input = test['k']
    expected = test['expected']
    actual = find_first_k_repeat(arr_input, k_input)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: arr={arr_input}, k={k_input}')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
