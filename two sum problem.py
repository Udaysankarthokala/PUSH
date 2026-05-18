arr = [2, 7, 11, 15]
target = 9

d = {}

for i in range(len(arr)):

    diff = target - arr[i]

    if diff in d:
        print(d[diff], i)

    d[arr[i]] = i