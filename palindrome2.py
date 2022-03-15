

def infinite_sequence():
    num = 0
    while True:
        # yield é um return, só que ele pode ser usado repetidas vezes.
        yield num
        num += 1


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


if __name__ == '__main__':
    # print(is_palindrome(110))
    for i in infinite_sequence():
        pal = is_palindrome(i)
        if pal:
            print(i)

