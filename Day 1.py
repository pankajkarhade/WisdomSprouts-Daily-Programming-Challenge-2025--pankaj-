def dnf(arr): 
    n = len(arr)
    if n == 0:
        return arr 
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            high-=1
    return arr
#Testing (from the document)
print("Test Cases:")
print("Test Case 1:")
Test_Case_1=[0, 1, 2, 1, 0, 2, 1, 0]
print(dnf(Test_Case_1))
Output_Test_Case_1=[0, 0, 0, 1, 1, 1, 2, 2];print(f"{'Pass' if Output_Test_Case_1==(Test_Case_1) else 'fail'}")
print("Test Case 2:")
Test_Case_2=[2, 2, 2, 2]
print(dnf(Test_Case_2))
Output_Test_Case_2=[2, 2, 2, 2];print(f"{'Pass' if Output_Test_Case_2==(Test_Case_2) else 'fail'}")
print("Test Case 3:")
Test_Case_3=[0, 0, 0, 0]
print(dnf(Test_Case_3))
Output_Test_Case_3=[0, 0, 0, 0];print(f"{'Pass' if Output_Test_Case_3==(Test_Case_3) else 'fail'}")
print("Test Case 4:")
Test_Case_4=[1, 1, 1, 1]
print(dnf(Test_Case_4))
Output_Test_Case_4=[1, 1, 1, 1];print(f"{'Pass' if Output_Test_Case_4==(Test_Case_4) else 'fail'}")
print("Test Case 5:")
Test_Case_5=[2, 0, 1]
print(dnf(Test_Case_5))
Output_Test_Case_5=[0, 1, 2];print(f"{'Pass' if Output_Test_Case_5==(Test_Case_5) else 'fail'}")
print("Test Case 6:")
Test_Case_6=[]
print(dnf(Test_Case_6))
Output_Test_Case_6=[];print(f"{'Pass' if Output_Test_Case_6==(Test_Case_6) else 'fail'}")
