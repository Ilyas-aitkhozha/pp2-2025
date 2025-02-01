def permutations(s):
    if len(s) <= 1:
        return [s]
    
    result = []
    for i in range(len(s)):
        current_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        for perm in permutations(remaining_chars):
            result.append(current_char + perm)
    return result


s = input("Enter your string: ")
print(permutations(s))
