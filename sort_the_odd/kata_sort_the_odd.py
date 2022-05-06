def backward_odd(array):
    for x in array[::-1]:
        if x %2 != 0:
            yield x

def sort_array(source_array):
    if source_array == []:
        return []
    backward = backward_odd(sorted(source_array, reverse=True))
    return list(map(lambda x: x if x%2 == 0 else next(backward), source_array))


def main():
    sort_array([5, 3, 1, 8, 0])

main()