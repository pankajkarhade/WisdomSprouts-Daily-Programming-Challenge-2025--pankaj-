def find_missing_number(arr):
  n = len(arr) + 1
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(arr)
  return expected_sum - actual_sum
  
test_cases = [
    {'input': [1, 2, 4, 5], 'expected': 3},
    {'input': [2, 3, 4, 5], 'expected': 1},
    {'input': [1, 2, 3, 4], 'expected': 5},
    {'input': [1], 'expected': 2},
    {'input': list(range(1, 1000000)), 'expected': 1000000}]

print("Running Test Cases :-")
for i, test in enumerate(test_cases):
    input_arr = test['input']
    expected_output = test['expected']
    actual_output = find_missing_number(input_arr)
    status = 'Pass' if actual_output == expected_output else 'Fail'
    print(f"\nTest Case {i + 1}:")
    if len(input_arr) > 20:
        print(f"Input: A list from 1 to {len(input_arr)}")
    else:
        print(f"Input: {input_arr}")
    print(f"Expected: {expected_output}, Actual: {actual_output}")
    print(f"Status: {status}")
print("\n**** Testing Complete ****")
