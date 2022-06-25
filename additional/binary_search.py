def lower_bound(mas, element):
    left, right = 0, len(mas)
    while right - left > 0:
        middle = (right + left) // 2
        if mas[middle] < element:
            left = middle + 1
        else:
            right = middle
    return left


def upper_bound(mas, element):
    left, right = 0, len(mas)
    while right - left > 0:
        middle = (right + left) // 2
        if mas[middle] <= element:
            left = middle + 1
        else:
            left = middle
    return left


def lower_bound_reverse(mas, element):
    left, right = -1, len(mas) - 1
    while right - left > 0:
        middle = (right + left + 1) // 2
        if mas[middle] > element:
            right = middle - 1
        else:
            left = middle
    return left


def upper_bound_reverse(mas, element):
    left, right = -1, len(mas) - 1
    while right - left > 0:
        middle = (right + left + 1) // 2
        if mas[middle] >= element:
            right = middle - 1
        else:
            left = middle
    return left
