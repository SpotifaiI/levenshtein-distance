def edit_distance(s1: str, s2: str) -> int:
    memo = {}  

    def dp(i: int, j: int) -> int:
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i

        if s1[i] == s2[j]:
            result = dp(i + 1, j + 1)
        else:
            insert_op = 1 + dp(i, j + 1)
            delete_op = 1 + dp(i + 1, j)
            replace_op = 1 + dp(i + 1, j + 1)
            result = min(insert_op, delete_op, replace_op)

        memo[(i, j)] = result
        return result

    return dp(0, 0)
