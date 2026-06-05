def longest_common_prefix(arr):

    prefix = arr[0]

    for word in arr[1:]:

        while not word.startswith(prefix):
            prefix = prefix[:-1]

    return prefix

print(longest_common_prefix(["flower","flow","flight"]))