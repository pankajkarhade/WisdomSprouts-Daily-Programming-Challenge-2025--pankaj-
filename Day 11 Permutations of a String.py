def find_permutations(s: str) -> list[str]:
  results = []
  chars = sorted(list(s))
  used = [False] * len(chars)
  def backtrack(current_permutation):
    if len(current_permutation) == len(chars):
      results.append("".join(current_permutation))
      return
    for i in range(len(chars)):
      if used[i]:
        continue
      if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
        continue
      used[i] = True
      current_permutation.append(chars[i])
      backtrack(current_permutation)
      current_permutation.pop()
      used[i] = False
  backtrack([])
  return results

test_cases = [
    {"input": "abc"},
    {"input": "aab"},
    {"input": "aaa"},
    {"input": "a"},]
for i, test in enumerate(test_cases):
    input_str = test['input']
    actual_output = find_permutations(input_str)
    print(f"\n--- Test Case {i + 1} ---")
    print(f"Input: '{input_str}'")
    print(f"Output: {sorted(actual_output)}")
