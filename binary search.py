arr = [1, 3, 5, 7, 9]

key = 7

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == key:
        print("Found")
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1