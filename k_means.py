def ro_measure(lens, means):
    """
    ro_measure:
        return quadratic measure between lens and means
    """
    return (abs(lens**2 - means**2)) ** 0.5


def ro_measure_2(lens, means):
    """
    ro_measure:
        return quadratic measure between lens and means
    """
    return (abs(lens**0.33 - means**0.33)) ** 0.5


def k_means_units(list_of_units):
    """
    k_means_units:
        define clasters for two type of sequinces of "1"
    """

    if len(list_of_units) == 0:
        return [], []

    min_th = min([len(x) for x in list_of_units])
    max_th = max([len(x) for x in list_of_units])
    claster1 = []
    claster3 = []
    check_length = 0
    while True:
        claster1.clear()
        claster3.clear()
        for current_vector in list_of_units:
            ro_1 = ro_measure(len(current_vector), min_th)
            ro_3 = ro_measure(len(current_vector), max_th)
            if ro_1 == min(ro_1, ro_3):
                claster1.append(current_vector)
            elif ro_3 == min(ro_1, ro_3):
                claster3.append(current_vector)
        min_th = (
            min_th
            if len(claster1) == 0
            else sum([len(x) for x in claster1]) / len(claster1)
        )
        max_th = (
            max_th
            if len(claster3) == 0
            else sum([len(x) for x in claster3]) / len(claster3)
        )
        if check_length == len(claster1):
            break
        else:
            check_length = len(claster1)

    return claster1, claster3

def k_means_units_means(list_of_units):
    """
    k_means_units:
        define clasters for two type of sequinces of "1"
    """

    if len(list_of_units) == 0:
        return [], []

    min_th = min([len(x) for x in list_of_units])
    max_th = max([len(x) for x in list_of_units])
    claster1 = []
    claster3 = []
    check_length = 0
    while True:
        claster1.clear()
        claster3.clear()
        for current_vector in list_of_units:
            ro_1 = ro_measure(len(current_vector), min_th)
            ro_3 = ro_measure(len(current_vector), max_th)
            if ro_1 == min(ro_1, ro_3):
                claster1.append(current_vector)
            elif ro_3 == min(ro_1, ro_3):
                claster3.append(current_vector)
        min_th = (
            min_th
            if len(claster1) == 0
            else sum([len(x) for x in claster1]) / len(claster1)
        )
        max_th = (
            max_th
            if len(claster3) == 0
            else sum([len(x) for x in claster3]) / len(claster3)
        )
        if check_length == len(claster1):
            break
        else:
            check_length = len(claster1)

    return min_th, max_th


def k_means_ziros(list_of_ziros):
    """
    k_means_ziros:
        define clasters for three type of sequinces of "0"
    """
    if len(list_of_ziros) == 0:
        return [], [], []

    if len(list_of_ziros) == 1:
        return [], list_of_ziros[0], []

    min_th = min([len(x) for x in list_of_ziros])
    max_th = max([len(x) for x in list_of_ziros])
    mid_th = (min_th + max_th) / 2

    claster1 = []
    claster3 = []
    claster6 = []
    check_length = 0

    while True:
        claster1.clear()
        claster3.clear()
        claster6.clear()
        for current_vector in list_of_ziros:
            ro_1 = ro_measure(len(current_vector), min_th)
            ro_3 = ro_measure(len(current_vector), mid_th)
            ro_6 = ro_measure(len(current_vector), max_th)
            if ro_1 == min(ro_1, ro_3, ro_6):
                claster1.append(current_vector)
            elif ro_3 == min(ro_1, ro_3, ro_6):
                claster3.append(current_vector)
            else:
                claster6.append(current_vector)
        min_th = (
            min_th
            if len(claster1) == 0
            else sum([len(x) for x in claster1]) / len(claster1)
        )
        mid_th = (
            mid_th
            if len(claster3) == 0
            else sum([len(x) for x in claster3]) / len(claster3)
        )
        max_th = (
            max_th
            if len(claster6) == 0
            else sum([len(x) for x in claster6]) / len(claster6)
        )
        if check_length == len(claster1):
            break
        else:
            check_length = len(claster1)

    return claster1, claster3, claster6


def k_means_ziros_units(list_of_ziros, list_of_units):
    """
    k_means_ziros:
        define clasters for three type of sequinces of "0"
    """
    if len(list_of_ziros) == 0:
        return [], [], []

    if len(list_of_ziros) == 1:
        return [], list_of_ziros[0], []

    min_th, mid_th = k_means_units_means(list_of_units)
    max_th = max([len(x) for x in list_of_ziros])


    claster1 = []
    claster3 = []
    claster6 = []
    check_length = 0

    claster1.clear()
    claster3.clear()
    claster6.clear()
    for current_vector in list_of_ziros:
        ro_1 = ro_measure(len(current_vector), min_th)
        ro_3 = ro_measure(len(current_vector), mid_th)
        ro_6 = ro_measure(len(current_vector), max_th)
        if ro_1 == min(ro_1, ro_3, ro_6):
            claster1.append(current_vector)
        elif ro_3 == min(ro_1, ro_3, ro_6):
            claster3.append(current_vector)
        else:
            claster6.append(current_vector)
    return claster1, claster3, claster6


def k_means_numbers(list_of_ziros):
    """
    k_means_ziros:
        define clasters for three type of sequinces of "0"
    """
    min_th = min(list_of_ziros)
    max_th = max(list_of_ziros)
    mid_th = (min_th + max_th) / 2
    
    claster1 = []
    claster3 = []
    claster6 = []
    check_length = 0

    while True:
        claster1.clear()
        claster3.clear()
        claster6.clear()
        for current_vector in list_of_ziros:
            ro_1 = ro_measure_2(current_vector, min_th)
            ro_3 = ro_measure_2(current_vector, mid_th)
            ro_6 = ro_measure_2(current_vector, max_th)
            if ro_1 == min(ro_1, ro_3, ro_6):
                claster1.append(current_vector)
            elif ro_3 == min(ro_1, ro_3, ro_6):
                claster3.append(current_vector)
            else:
                claster6.append(current_vector)
        min_th = (
            min_th if len(claster1) == 0 else sum([x for x in claster1]) // len(claster1)
        )
        mid_th = (
            mid_th if len(claster3) == 0 else sum([x for x in claster3]) // len(claster3)
        )
        max_th = (
            max_th if len(claster6) == 0 else sum([x for x in claster6]) // len(claster6)
        )
        if check_length == len(claster1):
            break
        else:
            check_length = len(claster1)
    if len(claster6) == 0:
        claster6.append(1000)
    return claster1, claster3, claster6


def main():
    pass


if __name__ == "main":
    main()
