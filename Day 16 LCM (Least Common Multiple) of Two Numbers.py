def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
  
def lcm(n, m):
  if n == 0 or m == 0:
    return 0
  common_divisor = gcd(n, m)
  return (n // common_divisor) * m

# Test Harness:-
test_cases = [
    {"n": 4, "m": 6, "expected": 12},
    {"n": 5, "m": 10, "expected": 10},
    {"n": 7, "m": 3, "expected": 21},
    {"n": 1, "m": 987654321, "expected": 987654321},
    {"n": 123456, "m": 789012, "expected": 8117355456},]
for i, test in enumerate(test_cases):
    n_input = test['n']
    m_input = test['m']
    expected = test['expected']
    actual = lcm(n_input, m_input)
    status = 'Pass' if actual == expected else 'Fail'
    print(f"\n--- Test Case {i + 1} ---")
    print(f'Input: N={n_input}, M={m_input}')
    print(f'Output: {actual} (Expected: {expected})')
    print(f"Status: {status}")
