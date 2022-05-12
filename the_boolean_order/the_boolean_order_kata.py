import itertools


operators = ['&', '|', '^']


def solve(s:str, ops:str):

    string = ''.join( [x for t in itertools.zip_longest(s,ops,fillvalue='') for x in t])
    print(string)
    stack = []



if __name__ == '__main__':
    solve("ttftff","|&^&&")