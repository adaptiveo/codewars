def maxlen(L1,L2):
    # return maximal length
    S1, S2 = max(L1, L2), min(L1, L2)
    T1, T2 = S1 / 3, S1 / 2
    if T1 >= S2:
        return T1
    else:
        return min(T2, S2)



print (maxlen(5,17))