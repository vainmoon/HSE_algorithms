def get_prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


def knuth_morris_pratt(s, w):
    if not w:
        return 0

    combined = w + "@" + s
    prefix = get_prefix(combined)
    m = len(w)

    for i in range(m + 1, len(combined)):
        if prefix[i] == m:
            return i - 2 * m
    return -1
