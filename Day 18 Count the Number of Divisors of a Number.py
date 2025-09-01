import math
def count_divisors(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  count = 0
  limit = int(math.sqrt(n))
  for i in range(1, limit + 1):
    if n % i == 0:      
      if i * i == n:
        count += 1
      else:
        count += 2      
  return count

#  Test  :-
test_cases = [
    {"input": 12, "expected": 6},
    {"input": 18, "expected": 6},
    {"input": 29, "expected": 2},
    {"input": 100, "expected": 9},
    {"input": 1, "expected": 1},
    {"input": 997, "expected": 2},]
for i, test in enumerate(test_cases):
    input_n = test['input']
    expected = test['expected']
    actual = count_divisors(input_n)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: N={input_n}')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
