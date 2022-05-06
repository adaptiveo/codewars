from scipy.signal import argrelextrema
import numpy as np
    

import k_means as km

def create_freq_dict(binary_list:list):
    binary_dict = {}
    lens_list = [len(x) for x in binary_list]
    for binary_element in range(1, max(lens_list)+1):
        binary_dict[binary_element] = lens_list.count(binary_element)
    return binary_dict

def create_freq_list(binary_list:list):
    lens_list = [len(x) for x in binary_list]
    freq_list = [0]*max(lens_list)
    for binary_element in range(0, max(lens_list)):
        freq_list[binary_element] = lens_list.count(binary_element + 1)
    return freq_list


def dict_parse(dicter: dict):
    claster_separators = []
    cl1, cl3, cl6 = km.k_means_numbers(list(dicter.keys()))
    claster_separators.append(max(cl1))
    claster_separators.append(max(cl3))
    claster_separators.append(max(cl6))
    return claster_separators


def dict_parse_2(dicter: dict):

    keyer = sorted(list(dicter.keys()))
    claster_separators = []
    for i in range(2, len(keyer) - 3):
        if dicter[keyer[i]] == min(
            dicter[keyer[i - 2]],
            dicter[keyer[i - 1]],
            dicter[keyer[i]],
            dicter[keyer[i + 1]],
            dicter[keyer[i + 2]],
        ):
            claster_separators.append(keyer[i])
    return claster_separators

def dict_parse_4(lister: list):

    claster_separators = []
    for i in range(2, len(lister) - 3):
        if lister[i] == min(
            lister[i - 2],
            lister[i - 1],
            lister[i],
            lister[i + 1],
            lister[i + 2],
        ):
            claster_separators.append(lister[i])
    return claster_separators


def dict_parse_3(dicter: dict):
    keyer = sorted(list(dicter.keys()))
    claster_separators = []
    
    old_val = 1000
    for k in keyer:
        if dicter[k] > old_val * 1.8:
            claster_separators.append(k)
        old_val = dicter[k]
    return claster_separators


def dict_parse_4(dicter: dict):
    x = np.array(list(dicter.keys()))
    z = argrelextrema(x, np.less)
    return list(z[0])

def dict_parse_5(lister: list):

    claster_separators = []
    for i in range(2, len(lister) - 3):
        if lister[i] == min(
            lister[i - 2],
            lister[i - 1],
            lister[i],
            lister[i + 1],
            lister[i + 2],
        ):
            claster_separators.append(i + 1)
    return claster_separators

def find_holes(keyer: list):
    return [x for x in range(max(keyer) + 1) if x not in keyer]


def main():
    pass


if __name__ == "__main__":
    main()
