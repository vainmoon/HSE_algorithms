def polynomial_hash(s, p=31, r=2**32):
    h = 0
    for ch in s:
        h = (h * p + ord(ch)) % r
    return h


def rabin_karp(s, w):
    n = len(s)
    m = len(w)
    p = 31
    r = 2**32
    w_hash = polynomial_hash(w, p, r)
    s_hash = polynomial_hash(s[:m], p, r)

    p_m = pow(p, m - 1, r)

    for i in range(n - m + 1):
        if s_hash == w_hash:
            if s[i : i + m] == w:
                return i
        if i >= n - m:
            break
        s_hash = ((s_hash - ord(s[i]) * p_m) * p + ord(s[i + m])) % r
    return -1
