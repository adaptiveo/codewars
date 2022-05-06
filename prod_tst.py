import itertools as it



a1 = "1"
a2 = "2"
a3 = "3"
a4 = "4"

aa = "aabb"

# print(["".join(p) for p in it.product(a1,a2,a3,a4)])

print(sorted(list(set(["".join(p) for p in it.permutations(aa)]))))

