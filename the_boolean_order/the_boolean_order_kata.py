import itertools
import time

operators = ['&', '|', '^']
forbiden = ['(t)', '(f)', '(&)', '(|)', '(^)', 't(', ')t', 'f(', ')f', ')(']
combinations = set()


def string_is_not_ok(current:str):
    return len([c for c in forbiden if c in current])


def generate_sequince(length:int, l:list, s:str):
    a = ['(', ')']
    if length == 0:
        if check_correctiveness(s):
            l.append(s)
        return ''
    for _ in range(2):
        generate_sequince(length-1, l, s + a[_])


def generate_string(predicats:str, brackets:str, candidate:str):
    if string_is_not_ok(candidate):
        return
    if len(predicats)==0:
        if check_correctiveness(candidate):
            combinations.add(candidate)
        return ''
    else:
        val1 = generate_string(predicats[1:], brackets, candidate + predicats[:1])
        if len(brackets)>0:
            val2 = generate_string(predicats, brackets[1:], candidate + brackets[:1])


def check_correctiveness(string:str):
    stack = []
    for c in string:
        if c == ')' and len(stack) == 0:
            return False
        if c == '(':
            stack.append(c)
        elif c == ')':
            stack.pop()
        else:
            continue
    if len(stack) > 0:
        return False
    else:
        return True


def solve(s:str, ops:str):
    brackets = []
    generate_sequince( ( len(s) - 2 ) * 2, brackets, '' )
    string = ''.join([x for t in itertools.zip_longest(s, ops, fillvalue='') for x in t])
    for br in brackets:
        print(generate_string(string, br, ''))
    print(len(combinations))
    counter = 0
    for c in combinations:
        if eval(c.replace('t','True').replace('f','False')):
            counter +=1
    return counter









if __name__ == '__main__':
    t = time.time()
    solve("ttftff","|&^&&")
    print(time.time() - t)
    print(combinations)
    # mass = []
    # generate_sequince(10,mass,'')
    # print(mass)

