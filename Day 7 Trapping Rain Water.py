def trap_rain_water(height):
  if len(height) < 3:
    return 0
  total_water = 0
  left, right = 0, len(height) - 1
  left_max, right_max = 0, 0
  while left <= right:
    if height[left] <= height[right]:
      if height[left] >= left_max:
        left_max = height[left]
      else:
        total_water += left_max - height[left]
      left += 1
    else: 
      if height[right] >= right_max:
        right_max = height[right]
      else:
        total_water += right_max - height[right]
      right -= 1
  return total_water

# Test Harness :-
test_cases = [
    {'input': [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 'expected': 6},
    {'input': [4, 2, 0, 3, 2, 5], 'expected': 9},
    {'input': [1, 1, 1], 'expected': 0},
    {'input': [5], 'expected': 0},
    {'input': [2, 0, 2], 'expected': 2},]

for i, test in enumerate(test_cases):
    input_arr = test['input']
    expected = test['expected']
    actual = trap_rain_water(input_arr)
    status = 'PAss' if actual == expected else 'FaiL'
    print(f"\n--- Test Case {i + 1} ---")
    print(f"INput: {input_arr}")
    print(f"TRapped Water: {actual} (Expected: {expected})")
    print(f"Status: {status}")
