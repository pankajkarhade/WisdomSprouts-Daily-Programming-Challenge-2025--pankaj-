def is_valid_parentheses(s: str) -> bool:
  stack = []
  bracket_map = {")": "(", "}": "{", "]": "["}
  for char in s:
    if char in bracket_map:
      top_element = stack.pop() if stack else '#'
      if bracket_map[char] != top_element:
        return False
    else:
      stack.append(char)
  return not stack

#  Test :-
test_cases = [
    {"input": "()", "expected": True},
    {"input": "([)]", "expected": False},
    {"input": "[{()}]", "expected": True},
    {"input": "", "expected": True},
    {"input": "{[}", "expected": False},
    {"input": "]", "expected": False},]
for i, test in enumerate(test_cases):
    input_str = test['input']
    expected = test['expected']
    actual = is_valid_parentheses(input_str)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: "{input_str}"')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
