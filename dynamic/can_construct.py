def can_construct(string, words):
    if string == "":
        return True

    for word in words:
        if string.startswith(word):
            if can_construct(string[len(word) :], words):
                return True

    # If no prefix can be used from the list of words
    return False


print("  Brute forse")
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(
#     can_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
#     )
# )


def can_construct(string, words, memo={}):
    if string in memo:
        return memo[string]
    if string == "":
        return True

    for word in words:
        if string.startswith(word):
            if can_construct(string[len(word) :], words, memo):
                memo[string] = True
                return True

    # If no prefix can be used from the list of words
    memo[string] = False
    return False


print("  Memoization")
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)


def can_construct_tab(string, words):
    table = [False for _ in range(len(string) + 1)]
    table[0] = True

    for i, _ in enumerate(table):
        if table[i] == True:
            suffix = string[i:]
            for word in words:
                if suffix.startswith(word):
                    table[i + len(word)] = True

    return table[-1]


print("  Tabulation")
print(can_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_construct_tab(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
