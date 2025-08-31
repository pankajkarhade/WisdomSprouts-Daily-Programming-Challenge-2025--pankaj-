import math
def prime_factorization(n: int) -> list[int]:
  factors = []
  while n % 2 == 0:
    factors.append(2)
    n //= 2
  d = 3
  while d * d <= n:
    while n % d == 0:
      factors.append(d)
      n //= d
    d += 2
  if n > 1:
    factors.append(n)    
  return factors

# Test  :-
test_cases = [
    {"input": 30, "expected": [2, 3, 5]},
    {"input": 49, "expected": [7, 7]},
    {"input": 19, "expected": [19]},
    {"input": 64, "expected": [2, 2, 2, 2, 2, 2]},
    {"input": 123456, "expected": [2, 2, 2, 2, 2, 3, 643]},]
for i, test in enumerate(test_cases):
    input_n = test['input']
    expected = test['expected']
    actual = prime_factorization(input_n)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: N={input_n}')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
