def all_construct(string, words):
    if string == "":
        return [[]]

    results = []
    for word in words:
        if string.startswith(word):
            suffix = string[len(word) :]
            suffix_constructs = all_construct(suffix, words)
            target_constructs = list(map(lambda x: [word] + x, suffix_constructs))
            results = results + target_constructs

    # If no prefix can be used from the list of words
    return results


# print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(
#     all_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
#     )
# )


def all_construct(string, words, memo={}):
    if string in memo:
        return memo[string]
    if string == "":
        return [[]]

    results = []
    for word in words:
        if string.startswith(word):
            suffix = string[len(word) :]
            suffix_constructs = all_construct(suffix, words, memo)
            target_constructs = list(map(lambda x: [word] + x, suffix_constructs))
            results = results + target_constructs

    # If no prefix can be used from the list of words
    memo[string] = results
    return results


print("  Memoization")
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(
#     all_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
#     )
# )


def all_construct_tab(string, words):
    table = [[] for _ in range(len(string) + 1)]
    table[0] = [[]]

    for i, _ in enumerate(table):
        if table[i] != []:
            suffix = string[i:]
            for word in words:
                if suffix.startswith(word):
                    table[i + len(word)] += [entry + [word] for entry in table[i]]

    return table[-1]


print("  Tabulation")
print(all_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(
#     all_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
#     )
# )
