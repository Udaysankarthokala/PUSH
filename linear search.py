arr = [2, 4, 6, 8, 10]

key = 8

for i in range(len(arr)):
    if arr[i] == key:
        print("Found at index", i)
        break
else:
    print("Not Found")