def reverse_stack(stack: list[int]):
  if stack:
    temp = stack.pop()    
    reverse_stack(stack)  
    insert_at_bottom(stack, temp)
    
def insert_at_bottom(stack: list[int], item: int): 
  if not stack:
    stack.append(item)
    return  
  top_element = stack.pop()
  insert_at_bottom(stack, item) 
  stack.append(top_element)

# Test :-
test_cases = [
    {"input": [1, 2, 3, 4]},
    {"input": [3, 2, 1]},
    {"input": [5]},
    {"input": [-5, -10, -15]},
    {"input": []},
    {"input": [3, 3, 3]},]
for i, test in enumerate(test_cases):
    stack_input = list(test['input']) # Create a copy for comparison
    expected_output = list(reversed(test['input']))    
    print(f"\n Test Case {i + 1} ")
    print(f'Original Stack (top is right): {stack_input}')    
    reverse_stack(stack_input)  
    status = 'Pass' if stack_input == expected_output else 'Fail'  
    print(f'Reversed Stack (top is right):   {stack_input}')
    print(f"Status: {status}")
