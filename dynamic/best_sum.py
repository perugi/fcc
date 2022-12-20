def best_sum(target, numbers):
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for number in numbers:
        remainder_result = best_sum(target - number, numbers)
        if remainder_result != None:
            remainder_result = remainder_result + [number]
            if shortest_combination == None or (
                len(remainder_result) < len(shortest_combination)
            ):
                shortest_combination = remainder_result

    return shortest_combination


def best_sum_memo(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for number in numbers:
        remainder_result = best_sum_memo(target - number, numbers, memo)
        if remainder_result != None:
            remainder_result = remainder_result + [number]
            if shortest_combination == None or (
                len(remainder_result) < len(shortest_combination)
            ):
                shortest_combination = remainder_result

    memo[target] = shortest_combination
    return memo[target]


# print(best_sum(7, [5, 4, 3, 7]))
# print(best_sum(8, [2, 5, 3]))
# print(best_sum(8, [5, 4, 1]))
# print(best_sum(100, [1, 2, 5, 25]))

print(best_sum_memo(7, [5, 4, 3, 7]))
print(best_sum_memo(8, [2, 5, 3]))
print(best_sum_memo(8, [5, 4, 1]))
print(best_sum_memo(100, [1, 2, 5, 25]))


def best_sum_tab(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i, _ in enumerate(table):
        if table[i] != None:
            for number in numbers:
                if i + number < len(table):
                    new = table[i] + [number]
                    current = table[i + number]
                    if current == None or len(new) < len(current):
                        table[i + number] = new

    return table[-1]


print(best_sum_tab(7, [5, 4, 3, 7]))
print(best_sum_tab(8, [2, 5, 3]))
print(best_sum_tab(8, [5, 4, 1]))
print(best_sum_tab(100, [1, 2, 5, 25]))
