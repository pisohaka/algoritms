def PatternUnlock(N: int, hits) -> str:
    matrix = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    distanse = 0
    for i in range(N):
        index_x, index_y = find_position(hits[i], matrix)
        if i == 0:
            prev_index_x = index_x
            prev_index_y = index_y
            continue
        if prev_index_x != index_x and prev_index_y != index_y:
            distanse = distanse + 2**(1/2)
        elif prev_index_x == index_x or prev_index_y == index_y:
            distanse = distanse + 1
        prev_index_x = index_x
        prev_index_y = index_y
    distanse = "%.5f" % distanse
    distanse = distanse.replace('.', '')
    distanse = distanse.replace('0', '')
    return distanse


def find_position(val, complex_list):
    for list_ in complex_list:
        if val in list_:
            x = complex_list.index(list_)
            y = list_.index(val)
    return x, y
