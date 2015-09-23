def split2(s, d):
    S = len(s)
    tmp, result = [], []

    for i in xrange(S):
        if s[i] == d:
            result.append(''.join(tmp))
            del tmp[:]
        else:
            tmp.append(s[i])

    result.append(''.join(tmp))

    return result


print split2("hola,mundo,dude", ",")
