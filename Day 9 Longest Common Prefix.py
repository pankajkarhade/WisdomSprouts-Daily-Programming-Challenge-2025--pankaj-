def longest_common_prefix(strs: list[str]) -> str:
  if not strs:
    return ""
  first_str = strs[0]
  for i, char in enumerate(first_str):
    for other_str in strs[1:]:
      if i >= len(other_str) or other_str[i] != char:
        return first_str[:i]
  return first_str

# Test Harness :-
test_cases = [
    {"input": ["flower", "flow", "flight"], "expected": "fl"},
    {"input": ["dog", "racecar", "car"], "expected": ""},
    {"input": ["apple", "ape", "april"], "expected": "ap"},
    {"input": [""], "expected": ""},
    {"input": ["alone"], "expected": "alone"},
    {"input": [], "expected": ""},]
for i, test in enumerate(test_cases):
    input_strs = test['input']
    expected = test['expected']
    actual = longest_common_prefix(input_strs)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\nTest Case {i + 1} :-")
    print(f'Input: {input_strs}')
    print(f'Output: "{actual}" (Expected: "{expected}")')
    print(f"Status: {status}")
