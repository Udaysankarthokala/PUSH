def find_duplicates(arr):

    seen = set()
    duplicates = []

    for num in arr:

        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

print(find_duplicates([4,3,2,7,8,2,3,1]))