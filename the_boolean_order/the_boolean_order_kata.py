import itertools


operators = ['&', '|', '^']


def generate_sequince(length:int, l:list, s:str):
    a = ['(', ')']
    if length == 0:
        if check_correctiveness(s):
            l.append(s)
        return ''
    for _ in range(2):
        generate_sequince(length-1, l, s + a[_])


def check_correctiveness(string:str):
    stack = []
    for c in string:
        if c == ')' and len(stack) == 0:
            return False
        if c == '(':
            stack.append(c)
        else:
            stack.pop()
    if len(stack) > 0:
        return False
    else:
        return True


def generate_evaluate_string(predicats:str, brackets:str):
    result = ''
    for i in range(len(brackets) - 1):
        result += brackets[i]
        if brackets[i] == '(' and brackets[i + 1] == ')':
            result += predicats[:3]
            predicats = predicats[3:]
        elif ( brackets[i] == ')' and brackets[i + 1] == ')' ) or ( brackets[i] == '(' and brackets[i + 1] == '(' ):
            result += predicats[:2]
            predicats = predicats[2:]
        elif brackets[i] == ')' and brackets[i + 1] == '(':
            result += predicats[:1]
            predicats = predicats[1:]
    result += brackets[-1:]
    return result

def solve(s:str, ops:str):
    brackets = []
    generate_sequince( ( len(s) - 2 ) * 2, brackets, '' )
    string = ''.join([x for t in itertools.zip_longest(s, ops, fillvalue='') for x in t])
    for br in brackets:
        print(generate_evaluate_string(string, br))




if __name__ == '__main__':
    solve("ttftff","|&^&&")
    mass = []
    generate_sequince(10,mass,'')
    print(mass)