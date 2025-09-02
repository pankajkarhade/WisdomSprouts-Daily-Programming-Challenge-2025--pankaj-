def evaluate_postfix(expression: str) -> int:
  stack = []
  tokens = expression.split()
  for token in tokens:
    if token.lstrip('-').isdigit():
      stack.append(int(token))
    else:
      operand2 = stack.pop()
      operand1 = stack.pop()
      if token == '+':
        stack.append(operand1 + operand2)
      elif token == '-':
        stack.append(operand1 - operand2)
      elif token == '*':
        stack.append(operand1 * operand2)
      elif token == '/':
        stack.append(int(operand1 / operand2))
    return stack.pop()

#  Tests :-
test_cases = [
    {"input": "2 1 + 3 *", "expected": 9},
    {"input": "5 6 +", "expected": 11},
    {"input": "-5 6 -", "expected": -11},
    {"input": "15 7 1 1 + - / 3 * 2 1 1 + + -", "expected": 5},
    {"input": "5", "expected": 5},
    {"input": "10 6 9 3 + -11 * / * 17 + 5 +", "expected": 22},]
for i, test in enumerate(test_cases):
    input_str = test['input']
    expected = test['expected']
    actual = evaluate_postfix(input_str)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n Test Case {i + 1} ---")
    print(f'Input: "{input_str}"')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
