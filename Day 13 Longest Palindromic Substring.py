def longest_palindromic_substring(s: str) -> str:
  if not s:
    return ""
  longest_palindrome = ""
  for i in range(len(s)):
    odd_palindrome = expand_from_center(s, i, i)
    if len(odd_palindrome) > len(longest_palindrome):
      longest_palindrome = odd_palindrome
    even_palindrome = expand_from_center(s, i, i + 1)
    if len(even_palindrome) > len(longest_palindrome):
      longest_palindrome = even_palindrome
  return longest_palindrome
def expand_from_center(s: str, left: int, right: int) -> str:
  while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1
  return s[left + 1:right]
# Test  :-
test_cases = [
    {"input": "babad", "expected": "bab"},
    {"input": "cbbd", "expected": "bb"},
    {"input": "a", "expected": "a"},
    {"input": "aaaa", "expected": "aaaa"},
    {"input": "abc", "expected": "a"},]
for i, test in enumerate(test_cases):
    input_str = test['input']
    expected = test['expected']
    actual = longest_palindromic_substring(input_str)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: "{input_str}"')
    print(f'Output: "{actual}" (Expected: "{expected}")')
    print(f"Status: {status}")
