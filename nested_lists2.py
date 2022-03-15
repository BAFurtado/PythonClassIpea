def nested_sum2(lists: list) -> (list, int):
    out = list()
    for l in lists:
        if type(l) == list:
            out += l
        else:
            out.append(l)
    try:
        sum(out)
    except TypeError:
        print(out)
        return nested_sum2(out)
    return out, sum(out)


if __name__ == '__main__':
    t2 = [[1, 2], [3], [4, 5, 6], [[[1, 2], [3], [4, 5, 6]]], 8, [[[[[78]]], [0, 9]], 11]]
    x, y = nested_sum2(t2)
