def count_construct(string, words):
    if string == "":
        return 1

    count = 0
    for word in words:
        if string.startswith(word):
            count += count_construct(string[len(word) :], words)

    return count


# print("  Brute force")
# print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(
#     count_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
#     )
# )


def count_construct(string, words, memo={}):
    if string in memo:
        return memo[string]
    if string == "":
        return 1

    count = 0
    for word in words:
        if string.startswith(word):
            count += count_construct(string[len(word) :], words)

    memo[string] = count
    return count


print("  Memoization")
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)


def count_construct_tab(string, words):
    table = [0 for _ in range(len(string) + 1)]
    table[0] = 1

    for i, _ in enumerate(table):
        if table[i] != 0:
            suffix = string[i:]
            for word in words:
                if suffix.startswith(word):
                    table[i + len(word)] += table[i]

    return table[-1]


print("  Tabulation")
print(count_construct_tab("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(
    count_construct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
)
print(
    count_construct_tab(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
