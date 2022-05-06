import itertools as it

def permutations(string):
    return sorted(list(set(["".join(p) for p in it.permutations(string)])))