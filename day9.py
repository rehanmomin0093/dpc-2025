def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)):
        j = 0
        while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
            j += 1
        prefix = prefix[:j]
        if prefix == "":
            return ""
    return prefix


strs = ["flower", "flow", "flight"]
result = longestCommonPrefix(strs)

if result == "":
    print('Output: ""')
else:
    print(f'Output: "{result}"')
