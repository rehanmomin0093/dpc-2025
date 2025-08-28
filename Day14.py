from collections import defaultdict

def count_substrings_with_exactly_k_distinct(s: str, k: int) -> int:
    def at_most_k(s, k):
        count = 0
        left = 0
        freq = defaultdict(int)
        distinct = 0

        for right in range(len(s)):
            if freq[s[right]] == 0:
                distinct += 1
            freq[s[right]] += 1

            while distinct > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    distinct -= 1
                left += 1

            count += (right - left + 1)
        return count

    if k > len(s) or k == 0:
        return 0

    return at_most_k(s, k) - at_most_k(s, k - 1)



print(count_substrings_with_exactly_k_distinct("pqpqs", 2))        
print(count_substrings_with_exactly_k_distinct("aabacbebebe", 3))  
print(count_substrings_with_exactly_k_distinct("a", 1))           
print(count_substrings_with_exactly_k_distinct("abc", 3))        
print(count_substrings_with_exactly_k_distinct("abc", 2))          
print(count_substrings_with_exactly_k_distinct("aaaa", 1))        
print(count_substrings_with_exactly_k_distinct("abc", 4))          
