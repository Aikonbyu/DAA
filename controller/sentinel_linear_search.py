def sentinelLinearSearch(array, key):
    last = array[len(array) - 1][0]
    array[len(array) - 1][0] = key
    i = 0
    while array[i][0] != key:
        i += 1
    array[len(array) - 1][0] = last
    if i < len(array) - 1 or last == key:
        return i
    else:
        return -1
