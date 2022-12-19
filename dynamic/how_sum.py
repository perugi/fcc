def how_sum(target, numbers):
    if target == 0:
        return []
    if target < 0:
        return None

    for number in numbers:
        remainder_result = how_sum(target - number, numbers)
        if remainder_result != None:
            return remainder_result + [number]

    return None


def how_sum_memo(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for number in numbers:
        remainder_result = how_sum_memo(target - number, numbers, memo)
        if remainder_result != None:
            memo[target] = remainder_result + [number]
            return memo[target]

    memo[target] = None
    return memo[target]


print(how_sum(7, [5, 4, 3, 7]))
print(how_sum(6, [5, 4, 7]))
print(how_sum(8, [2, 4, 7]))
# print(how_sum(300, [7, 14]))

print(how_sum_memo(7, [5, 4, 3, 7]))
print(how_sum_memo(6, [5, 4, 7]))
print(how_sum_memo(8, [2, 4, 7]))
print(how_sum_memo(300, [7, 14]))
