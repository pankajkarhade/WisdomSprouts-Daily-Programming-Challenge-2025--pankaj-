def sort_stack(stack: list[int]):
  if not stack:
    return
  temp = stack.pop()
  sort_stack(stack)
  insert_sorted(stack, temp)

def insert_sorted(stack: list[int], item: int):
  if not stack or stack[-1] <= item:
    stack.append(item)
    return
  top_element = stack.pop()
  insert_sorted(stack, item)
  stack.append(top_element)

# Test :-
test_cases = [
    {"input": [3, 1, 4, 2]},
    {"input": [7, 1, 5]},
    {"input": [5]},
    {"input": [-3, 14, 8, 2]},
    {"input": []},
    {"input": [3, 3, 3]},]
for i, test in enumerate(test_cases):
    stack_input = test['input']
    print(f"\nTest Case:- {i + 1} -:")
    print(f'Original Stack (top is right): {stack_input}')
    sort_stack(stack_input)
    expected = sorted(test['input'])
    status = 'Pass' if stack_input == expected else 'Fail'
    print(f'Sorted Stack (top is right):   {stack_input}')
    print(f'Status: {status}')
