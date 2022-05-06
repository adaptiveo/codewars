def generate_num_pad():
    neigbors_dict = {}
    num_pad=[[0]*5 for _ in range(5)]
    counter = 1
    for i in range(1,4):
        for j in range(1,4):
            num_pad[i][j] = str(counter)
            counter += 1
    for i in range(1,4):
        for j in range(1,4):
            temp_list = set()
            for s in range (-1,2):
                if num_pad[i+s][j]:
                    temp_list.add(num_pad[i+s][j])
                if num_pad[i][j+s]:
                    temp_list.add(num_pad[i][j+s])
            neigbors_dict[num_pad[i][j]] = sorted(list(temp_list))
    neigbors_dict['0'] = ['0', '8']
    return neigbors_dict

neighbors_dict = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['5', '7', '8', '9', '0'],
    '9': ['6', '8', '9'],
    '0': ['0', '8']
}

megalist = []

def get_pins_reсursive(observed:list, result:list, counter:int):
    global megalist
    if len(observed) == counter:
        megalist.append("".join(result))
        return
    tup = observed[counter]
    for el in neighbors_dict[tup]:
        result.append(el)
        get_pins_reсursive(observed, result, counter + 1)
        result.pop()


def get_pins(observed):
    global megalist
    megalist = []
    get_pins_reсursive(list(observed), [], 0)
    return megalist


def main():
    print(get_pins("8"))


main()
