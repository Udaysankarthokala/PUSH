def peak_element(arr):

    n = len(arr)

    for i in range(n):

        left = arr[i-1] if i > 0 else float('-inf')
        right = arr[i+1] if i < n-1 else float('-inf')

        if arr[i] >= left and arr[i] >= right:
            return arr[i]

print(peak_element([1,3,20,4,1,0]))