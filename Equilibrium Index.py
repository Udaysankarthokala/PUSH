def equilibrium_index(nums):

    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)):

        total -= nums[i]

        if left_sum == total:
            return i

        left_sum += nums[i]

    return -1

print(equilibrium_index([1,7,3,6,5,6]))