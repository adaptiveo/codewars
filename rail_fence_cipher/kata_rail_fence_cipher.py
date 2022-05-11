import itertools


def direction_3(n):
    i, delta = 0, 1
    while True:
        yield i
        if (i == n - 1 and delta == 1) or (i == 0 and delta == -1):
            delta = -1 * delta
        i += delta


def rail_fence(collection, n):
    ddd = [[] for i in range(n)]
    rail = direction_3(n)
    for i in collection:
        ddd[next(rail)].append(i)
    return itertools.chain.from_iterable(ddd)


def encode_rail_fence_cipher(string: str, n: int) -> str:
    if len(string) == 0:
        return ''
    return ''.join(rail_fence(string, n))


def decode_rail_fence_cipher(string: str, n: int) -> str:
    if len(string) == 0:
        return ''

    array = [''] * len(string)

    for c, i in zip(string, list(rail_fence(range(len(string)), n))):
        array[i] = c

    return ''.join(array)


'''
def decode_rail_fence_cipher_old(string: str, n: int) -> str:
    if len(string) == 0:
        return ''

    pas = False if len(string) % (2 * n - 2) > n else True

    array = list(string)
    p1 = (math.ceil(len(array) / (2 * n - 2)))
    p2 = (math.ceil((len(array) - n + 1) / (2 * n - 2)))
    mass = [array[:p1], array[-p2:]]
    m_m = array[p1:-p2]
    mid_rail = n - 2
    for r in range(mid_rail, 0, -1):
        r_l = math.ceil(len(m_m) / r)
        if pas:
            m_1, m_m = m_m[:r_l], m_m[r_l:]
            mass.insert(mid_rail - r + 1, m_1)
        else:
            m_1, m_m = m_m[-r_l:], m_m[:-r_l]
            mass.insert(1, m_1)

    print(mass)
    rail = direction_3(n)
    new_string = ''.join([mass[next(rail)].pop(0) for _ in string])
    return new_string
'''

if __name__ == '__main__':
    print(decode_rail_fence_cipher(encode_rail_fence_cipher("12345678901234567", 4), 4))
