def find_leaders(arr):
  n = len(arr)
  if n == 0:
    return []
  leaders = []
  max_from_right = arr[n - 1]
  leaders.append(max_from_right)
  for i in range(n - 2, -1, -1):
    current_element = arr[i]
    if current_element > max_from_right:
      leaders.append(current_element)
      max_from_right = current_element
  leaders.reverse()
  return leaders

test_cases = [
    {'input': [16, 17, 4, 3, 5, 2], 'expected': [17, 5, 2]},
    {'input': [1, 2, 3, 4, 0], 'expected': [4, 0]},
    {'input': [7, 10, 4, 10, 6, 5, 2], 'expected': [10, 6, 5, 2]},
    {'input': [5], 'expected': [5]},
    {'input': [100, 50, 20, 10], 'expected': [100, 50, 20, 10]},
    {'input': list(range(1, 1000001)), 'expected': [1000000]}]

for i, test in enumerate(test_cases):
    input_arr = test['input']
    expected = test['expected']
    actual = find_leaders(input_arr)
    status = 'PasS' if actual == expected else 'FAil'
    print(f"\nTest Case {i + 1}:")
    if len(input_arr) > 20:
        print(f"Input: A list from {input_arr[0]} to {input_arr[-1]}")
    else:
        print(f"Input: {input_arr}")  
    print(f"LEaders: {actual}")
    print(f"StaTus: {status}")
