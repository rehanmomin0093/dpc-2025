def length_of_longest_substring(S: str) -> int:
    char_index = {}
    max_length = 0
    start = 0 

    for end in range(len(S)):
        if S[end] in char_index and char_index[S[end]] >= start:
            start = char_index[S[end]] + 1  

        char_index[S[end]] = end  
        max_length = max(max_length, end - start + 1)

    return max_length


print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))     
print(length_of_longest_substring("pwwkew"))     
print(length_of_longest_substring("abcdefgh"))   
print(length_of_longest_substring("a"))          
