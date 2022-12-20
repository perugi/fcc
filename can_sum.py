def can_sum(target, numbers):
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        if can_sum(target - number, numbers):
            return True

    return False


def can_sum_memo(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        if can_sum_memo(target - number, numbers, memo):
            memo[target] = True
            return memo[target]

    memo[target] = False
    return memo[target]


# print(can_sum(7, [5, 4, 3, 7]))
# print(can_sum(6, [5, 4, 7]))
# print(can_sum(300, [7, 14]))

print(can_sum_memo(7, [5, 4, 3, 7]))
print(can_sum_memo(6, [5, 4, 7]))
print(can_sum_memo(300, [7, 14]))


def can_sum_tab(target, numbers):
    table = [False for _ in range(target + 1)]
    table[0] = True

    for i, _ in enumerate(table):
        if table[i] == True:
            for number in numbers:
                if i + number < len(table):
                    table[i + number] = True

    return table[-1]


print(can_sum_tab(7, [5, 4, 3, 7]))
print(can_sum_tab(6, [5, 4, 7]))
print(can_sum_tab(300, [7, 14]))
