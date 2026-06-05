def longest_palindrome(s):

    result = ""

    for i in range(len(s)):

        l = r = i

        while l >= 0 and r < len(s) and s[l] == s[r]:

            if r - l + 1 > len(result):
                result = s[l:r+1]

            l -= 1
            r += 1

    return result

print(longest_palindrome("babad"))