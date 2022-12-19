def grid_travel(m, n):
    """m, n are dimensions of the grid
    returns the number of ways that the grid can be traversed"""

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    return grid_travel(m - 1, n) + grid_travel(m, n - 1)


def grid_travel_memo(m, n, memo={}):
    """m, n are dimensions of the grid
    returns the number of ways that the grid can be traversed"""

    key = f"{m},{n}"
    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = grid_travel_memo(m - 1, n, memo) + grid_travel_memo(m, n - 1, memo)
    return memo[key]


# print(grid_travel(1, 3))
# print(grid_travel(2, 3))
# print(grid_travel(20, 20))

print(grid_travel_memo(1, 3))
print(grid_travel_memo(2, 3))
print(grid_travel_memo(20, 20))
