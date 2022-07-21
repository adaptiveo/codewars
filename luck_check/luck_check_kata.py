import string
from functools import reduce



def luck_check(s):
    l_s = len(s)
    if (l_s == 0) or (len(set(s).difference(set(string.digits))) > 0):
        raise Exception("wrong input string")
    m_s = l_s // 2
    return reduce(lambda x, y: int(x)+int(y), s[:m_s]) == reduce(lambda x, y: int(x)+int(y), s[l_s - m_s:])
