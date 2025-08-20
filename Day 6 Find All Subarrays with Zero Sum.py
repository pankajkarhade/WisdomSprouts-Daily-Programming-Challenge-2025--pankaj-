import collections
def find_zero_sum_subarrays(arr):
  prefix_sum_map = collections.defaultdict(list)
  result = []
  current_sum = 0
  for i, num in enumerate(arr):
    current_sum += num
    if current_sum == 0:
      result.append((0, i))
    if current_sum in prefix_sum_map:
      for start_index in prefix_sum_map[current_sum]:
        result.append((start_index + 1, i))
    prefix_sum_map[current_sum].append(i)
  return result
test_cases = [
    {'input': [1, 2, -3, 3, -1, -2]}, 
    {'input': [4, -1, -3, 1, 2, -1]},
    {'input': [1, 2, 3, 4]},
    {'input': [0, 0, 0]},
    {'input': [-3, 1, 2, -3, 4, 0]},]
for i, test in enumerate(test_cases):
    input_arr = test['input']
    actual_output = find_zero_sum_subarrays(input_arr)
    print(f"\n--- Test Case {i + 1} ---")
    print(f"Input: {input_arr}")
    print(f"Output: {actual_output}")
