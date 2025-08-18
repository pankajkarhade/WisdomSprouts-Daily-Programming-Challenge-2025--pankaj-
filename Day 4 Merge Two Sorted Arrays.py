def merge_sorted_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    total_len = m + n
    gap = (total_len + 1) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < total_len:
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]
            elif i >= m and j >= m:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]
            i += 1
            j += 1
        if gap == 1:
            break
        gap = (gap + 1) // 2

if __name__ == "__main__":
    test_cases = [
        {"id": 1, "arr1": [1, 3, 5], "arr2": [2, 4, 6], "expected1": [1, 2, 3], "expected2": [4, 5, 6]},
        {"id": 2, "arr1": [10, 12, 14], "arr2": [1, 3, 5], "expected1": [1, 3, 5], "expected2": [10, 12, 14]},
        {"id": 3, "arr1": [2, 3, 8], "arr2": [4, 6, 10], "expected1": [2, 3, 4], "expected2": [6, 8, 10]},
        {"id": 4, "arr1": [1], "arr2": [2], "expected1": [1], "expected2": [2]},
        {"id": 5, "arr1": [1, 5, 9, 10], "arr2": [2, 3, 8], "expected1": [1, 2, 3, 5], "expected2": [8, 9, 10]},
    ]
    print("Running Test Cases for Merge Sorted Arrays :-")
    for case in test_cases:
        arr1_orig = list(case["arr1"])
        arr2_orig = list(case["arr2"])
        print(f"\n## Test Case {case['id']}:")
        print(f"   input: arr1 = {arr1_orig}, arr2 = {arr2_orig}")
        merge_sorted_arrays(case["arr1"], case["arr2"])
        print(f"   output:  arr1 = {case['arr1']}, arr2 = {case['arr2']}")
        is_passed = case["arr1"] == case["expected1"] and case["arr2"] == case["expected2"]
        result = "PAss" if is_passed else "FaileD"
        print(f"   Result: {result}")
