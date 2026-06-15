def find_pair(arr, target):

    seen = set()

    for num in arr:

        if target - num in seen:
            return (target - num, num)

        seen.add(num)

    return None

print(find_pair([8,7,2,5,3,1], 10))