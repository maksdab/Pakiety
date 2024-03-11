is_palindrome = lambda s: s.lower().replace(" ", "") == s.lower().replace(" ", "")[::-1]


print(is_palindrome("kajak"))  
print(is_palindrome("A man a plan a canal Panama"))  
print(is_palindrome("Python"))  
print(is_palindrome("radar"))  