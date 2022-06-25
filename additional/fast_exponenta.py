def fast_exp(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif k % 2 == 0:
        return fast_exp(n ** 2, k // 2)
    else:
        return n * fast_exp(n, k - 1)
