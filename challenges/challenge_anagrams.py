def is_anagram(first_string, second_string):
    first = combine_sort(first_string.lower())
    second = combine_sort(second_string.lower())
    if len(first) < 1 or len(second) < 1:
        return first, second, False
    return (
        first,
        second,
        set(first) == set(second) and len(first) == len(second),
    )


def merge(left, right):
    start, end = 0, 0
    word = []
    while start < len(left) and end < len(right):
        if left[start] < right[end]:
            word.append(left[start])
            start += 1
        else:
            word.append(right[end])
            end += 1
    word += left[start:] if start < len(left) else right[end:]
    return "".join(word)


def combine_sort(string):
    if len(string) > 1:
        mid = len(string) // 2
        left = combine_sort(string[:mid])
        right = combine_sort(string[mid:])
        string = merge(left, right)
    return string
