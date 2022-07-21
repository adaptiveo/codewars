import string


def luck_check(s):
    l_s = len(s)
    if (l_s == 0) or (len(set(s).difference(set(string.digits))) > 0):
        raise Exception("wrong input string")
    if l_s % 2 == 1:
        return False
    sum_left, sum_right = 0, 0
    for i in range(l_s // 2):
        sum_left += int(s[i])
        sum_right += int(s[l_s - 1 - i])
    return sum_left == sum_right
