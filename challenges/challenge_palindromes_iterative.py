def is_palindrome_iterative(word):
    i = 0
    if len(word) == 0:
        return False

    for index in word:
        if index == word[i - 1]:
            i -= 1
        else:
            return False
    return True
