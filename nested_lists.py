

def nested_sum1(lists: list) -> int:
    out = 0
    for l in lists:
        out += sum(l)
    return out


if __name__ == '__main__':
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum1(t))

