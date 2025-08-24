from collections import defaultdict

def groupAnagrams(strs):
    # Dictionary to hold grouped anagrams
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the word → same anagrams will have the same sorted key
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

  
    return list(anagram_map.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


print(groupAnagrams([""]))

print(groupAnagrams(["a"]))

print(groupAnagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))

print(groupAnagrams(["abc", "def", "ghi"]))

