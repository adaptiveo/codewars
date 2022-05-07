import math


def direction_3(n):
    x,dx = 0,1
    while True:
        yield x
        if (x == n-1 and dx == 1) or (x == 0 and dx == -1):
            dx = -1 * dx
        x += dx


def encode_rail_fence_cipher(string: str, n: int) -> str:
    if len(string) == 0:
        return ''

    ddd = [[] for i in range(n)]
    rail = direction_3(n)
    for i in string:
        ddd[next(rail)].append(i)
    print(ddd)
    return ''.join([''.join(d) for d in ddd])


def decode_rail_fence_cipher(string: str, n: int) -> str:
    if len(string) == 0:
        return ''

    pas = True
    if len(string) % (2 * n - 2) > n:
        pas = False

    array = list(string)
    p1 = (math.ceil(len(array) / (2 * n - 2)))
    p2 = (math.ceil((len(array) - n + 1) / (2 * n - 2)))
    mass = []
    m_s = array[:p1]
    m_f = array[-p2:]
    mass.append(m_s)
    mass.append(m_f)
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
    new_string = ''
    for _ in string:
        new_string += str(mass[next(rail)].pop(0))
    return new_string


# print(encode_rail_fence_cipher("1234567890123456789012345678901234567890",4))
print(decode_rail_fence_cipher(encode_rail_fence_cipher("12345678901234567", 4), 4))
