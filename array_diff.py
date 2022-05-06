'''
вычисление разности двух массивов с набором тестов
'''

def array_diff(first_array:list, second_array:list) -> list:
    '''
    array_diff:
        вычисление разности массивов
    '''
    return [x for x in first_array if x not in second_array]


