def reverse_words(s: str) -> str:
  
    words = s.strip().split()
    
    words.reverse()
  
    return " ".join(words)

s = input("Enter string: ")
print(reverse_words(s))
