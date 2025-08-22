def reverse_words(s: str) -> str:
  words = s.split()
  reversed_words = words[::-1]
  return " ".join(reversed_words)

test_cases = [
    {"input": "the sky is blue", "expected": "blue is sky the"},
    {"input": "  hello world  ", "expected": "world hello"},
    {"input": "a good   example", "expected": "example good a"},
    {"input": "      ", "expected": ""},
    {"input": "word", "expected": "word"},]
for i, test in enumerate(test_cases):
    input_str = test['input']
    expected = test['expected']
    actual = reverse_words(input_str)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n Test Case {i + 1} :-")
    print(f'Input: "{input_str}"')
    print(f'Output: "{actual}" (Expected: "{expected}")')
    print(f"Status: {status}")
