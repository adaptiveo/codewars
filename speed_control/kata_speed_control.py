x = [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]
s = 12

def gps(s, x):
    return 0 if len(x) <=1 else max(list(map(lambda p,q: int(3600 * (p-q) / s), x[1:], x[:-1])))



print (gps(12,x))

