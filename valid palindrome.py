def is_palindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))