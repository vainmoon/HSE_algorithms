def get_lcs(string_1, string_2):
    m, n = len(string_1), len(string_2)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string_1[i - 1] == string_2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if string_1[i - 1] == string_2[j - 1]:
            lcs.append(string_1[i - 1])
            i -= 1
            j -= 1
        else:
            if table[i - 1][j] >= table[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return "".join(reversed(lcs))
