def first_missing_positive(nums):

    s = set(nums)

    i = 1

    while True:
        if i not in s:
            return i
        i += 1

print(first_missing_positive([3,4,-1,1]))