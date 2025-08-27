def longest_palindromic_substring(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the valid palindrome slice

    longest = ""
    for i in range(len(s)):
     
        odd = expand_around_center(i, i)
       
        even = expand_around_center(i, i + 1)
         if len(odd) > len(longest):
            longest = odd
         if len(even) > len(longest):
            longest = even

    return longest


print(longest_palindromic_substring("babad"))  
print(longest_palindromic_substring("cbbd")) 
print(longest_palindromic_substring("a"))     
print(longest_palindromic_substring("aaaa"))
print(longest_palindromic_substring("abc"))  
