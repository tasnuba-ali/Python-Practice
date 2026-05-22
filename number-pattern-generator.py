def number_pattern (n):
    if not isinstance(n, int) or isinstance(n, bool):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    result = ""
    for i in range(1, n + 1):
        if i == 1:
            result = str(i)
        else:
            result = result + " " + str(i)

    return result
